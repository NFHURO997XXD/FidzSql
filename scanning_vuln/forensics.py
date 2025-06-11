import requests
from bs4 import BeautifulSoup
import whois
import ssl
import socket
from urllib.parse import urlparse

# Fungsi untuk mengambil metadata dari halaman website
def get_website_metadata(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ambil title halaman
        title = soup.title.string if soup.title else "Title tidak ditemukan"

        # Ambil meta description
        description = soup.find('meta', attrs={'name': 'description'})
        description_content = description['content'] if description else "Description tidak ditemukan"

        # Ambil meta keywords
        keywords = soup.find('meta', attrs={'name': 'keywords'})
        keywords_content = keywords['content'] if keywords else "Keywords tidak ditemukan"

        print(f"\n=== Metadata Website {url} ===")
        print(f"Title       : {title}")
        print(f"Description : {description_content}")
        print(f"Keywords    : {keywords_content}")

    except Exception as e:
        print(f"Error mengambil metadata: {e}")

# Fungsi untuk mendapatkan header HTTP dari website
def get_http_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers

        print(f"\n=== HTTP Headers {url} ===")
        for key, value in headers.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error mengambil HTTP headers: {e}")

# Fungsi untuk mengambil informasi SSL dari website
def get_ssl_info(domain):
    try:
        context = ssl.create_default_context()
        conn = context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=domain,
        )
        conn.connect((domain, 443))
        ssl_info = conn.getpeercert()

        print(f"\n=== Informasi SSL untuk {domain} ===")
        print(f"Issuer: {ssl_info['issuer']}")
        print(f"Valid From: {ssl_info['notBefore']}")
        print(f"Valid Until: {ssl_info['notAfter']}")
    except Exception as e:
        print(f"Error mengambil informasi SSL: {e}")

# Fungsi untuk mendapatkan informasi whois domain
def get_whois_info(domain):
    try:
        domain_info = whois.whois(domain)
        print(f"\n=== Informasi WHOIS untuk {domain} ===")
        print(f"Domain Name : {domain_info.domain_name}")
        print(f"Registrar   : {domain_info.registrar}")
        print(f"Creation Date: {domain_info.creation_date}")
        print(f"Expiration Date: {domain_info.expiration_date}")
        print(f"Name Servers: {domain_info.name_servers}")
    except Exception as e:
        print(f"Error mengambil informasi WHOIS: {e}")

# Fungsi utama untuk forensik website
def forensic_website_info(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc if parsed_url.netloc else parsed_url.path

    print(f"\nMulai forensik website: {url}\n")
    
    # Mendapatkan metadata website
    get_website_metadata(url)
    
    # Mendapatkan header HTTP
    get_http_headers(url)
    
    # Mendapatkan informasi SSL
    get_ssl_info(domain)
    
    # Mendapatkan informasi WHOIS domain
    get_whois_info(domain)

# Input URL dari pengguna
website_url = input("Masukkan URL website (contoh: https://example.com): ")

# Menjalankan fungsi forensik website
forensic_website_info(website_url)