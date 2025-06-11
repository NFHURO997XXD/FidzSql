"""
En:
Made by adjidev
open source
Forbidden if deleted the watermark

Id:
Dibuat oleh adjideb
Gratis
Jika watermark dihapus saya gak akan ngeshare tools lagi
"""


import argparse
import sys
import time
from urllib.error import HTTPError, URLError
import urllib.request
from bs4 import BeautifulSoup
import ssl
import threading

# [+]================================================================[+]
red = '\033[31m'       
green = '\033[32m'     
yellow = '\033[33m'    
blue = '\033[34m'      
magenta = '\033[35m'   
cyan = '\033[36m'      
white = '\033[37m'     
black = '\033[30m'     
bright_red = '\033[91m' 
bright_green = '\033[92m'
bright_yellow = '\033[93m' 
bright_blue = '\033[94m'   
bright_magenta = '\033[95m' 
bright_cyan = '\033[96m'    
bright_white = '\033[97m'   
bg_black = '\033[40m'    
bg_red = '\033[41m'      
bg_green = '\033[42m'    
bg_yellow = '\033[43m'   
bg_blue = '\033[44m'     
bg_magenta = '\033[45m'  
bg_cyan = '\033[46m'     
bg_white = '\033[47m'    
reset = '\033[0m'

banner = r"""
__________________________________________________    __
___    |__  __ \_____  /___  _/__  __ \__  ____/_ |  / /
__  /| |_  / / /__ _  / __  / __  / / /_  __/  __ | / / 
_  ___ |  /_/ // /_/ / __/ /  _  /_/ /_  /___  __ |/ /  
/_/  |_/_____/ \____/  /___/  /_____/ /_____/  _____/   
                     @adjisan
"""

ingfo = f"""{yellow}TELEGRAM{reset} :  https://t.me/adjidev\n\n\n"""

sslContent = ssl._create_unverified_context()

medsos = [
    {"url": "https://www.twitter.com/{}", "name": "Twitter"},
    {"url": "https://www.instagram.com/{}", "name": "Instagram"},
    {"url": "https://www.github.com/{}", "name": "GitHub"},
    {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
    {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
    {"url": "https://www.youtube.com/{}", "name": "YouTube"},
    {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
    {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
    {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
    {"url": "https://www.behance.net/{}", "name": "Behance"},
    {"url": "https://www.medium.com/@{}", "name": "Medium"},
    {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
    {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
    {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
    {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
    {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
    {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
    {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
    {"url": "https://www.telegram.me/{}", "name": "Telegram"},
    {"url": "https://www.weheartit.com/{}", "name": "We Heart It"},
    {"url": "https://www.reddit.com/user/{}", "name": "Reddit"},
    {"url": "https://www.discord.com/{}", "name": "Discord"},
    {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
    {"url": "https://www.clubhouse.com/@{}", "name": "Clubhouse"},
    {"url": "https://www.mix.com/{}", "name": "Mix"},
    {"url": "https://www.yelp.com/user_details?userid={}", "name": "Yelp"},
    {"url": "https://www.reverbnation.com/{}", "name": "ReverbNation"},
    {"url": "https://www.soundcloud.com/{}", "name": "SoundCloud"},
    {"url": "https://www.foursquare.com/{}", "name": "Foursquare"},
    {"url": "https://www.meetup.com/members/{}", "name": "Meetup"},
    {"url": "https://www.slack.com/{}", "name": "Slack"},
    {"url": "https://www.goodreads.com/{}", "name": "Goodreads"}
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Connection": "keep-alive",
}

def Loading(delay=0.012):
    spinner = ['|', '/', '-', '\\']
    while not stop_loading[0]:  
        for symbol in spinner:
            sys.stdout.write(f'\r{symbol} Checking the page')  
            sys.stdout.flush()  
            time.sleep(delay)
    sys.stdout.write(f'\r{green}√{reset} Success            \n')

def CheckPages(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        adjisan = urllib.request.urlopen(req, context=sslContent)
        PagesContent = adjisan.read()

        if adjisan.getcode() == 404:
            return True

        soup = BeautifulSoup(PagesContent, 'html.parser')

        not_found_texts = [
            "This page doesn’t exist", "Page not found", 
            "Sorry, we couldn’t find that page", 
            "We’re sorry. Something went wrong on this page.", "404"
        ]
        
        for text in not_found_texts:
            if soup.body and text.lower() in soup.body.get_text().lower():
                return True
        return False
    except HTTPError as e:
        if e.code == 404:
            return True
        pass
        return True
    except URLError as e:
        pass
        return True
    except Exception as e:
        pass
        return True

def Adjidev(username, simpan=None):
    data = []
    print(red + banner + reset)
    print(ingfo)
    print(f"[ {yellow}INFO{reset} ] Searching username: {username}\n")
    for platform in medsos:
        profile_url = platform["url"].format(username)
        print(f"{yellow}{platform['name']}: {blue}{profile_url}{reset}")
        
        stop_loading[0] = False
        loading_thread = threading.Thread(target=Loading, args=(0.1,))
        loading_thread.start()

        try:
            if CheckPages(profile_url):
                stop_loading[0] = True
                loading_thread.join()
                print(f"[ {red}NOT FOUND{reset} ] {platform['name']}\n")
            else:
                stop_loading[0] = True 
                loading_thread.join()
                rslt = f"Type: {platform['name']}\nName: {username}\nUrl: {profile_url}\n=========================\n"
                print(f"[ {green}FOUND{reset} ] {platform['name']}\n")
                data.append(rslt)
        except KeyboardInterrupt:
            stop_loading[0] = True 
            loading_thread.join()
            print(f"\n[ {red}EXIT{reset} ]")
        except Exception as e:
            stop_loading[0] = True 
            loading_thread.join()
            pass

        if simpan:
            with open(simpan, 'w') as f:
                f.writelines(data)
                #print(f'[ {yellow}INFO{reset} ] Saving to \'{simpan}\'')

def main():
    parser = argparse.ArgumentParser(description='Search for a username across various social media platforms.')
    parser.add_argument('--search', type=str, required=True, help='The username to search for on social media.')
    parser.add_argument('--save', type=str, help='File to save the result')

    args = parser.parse_args()
    Adjidev(args.search, args.save)

stop_loading = [False]

if __name__ == "__main__":
    main()
