import socket
import sys

def scan_ports(host, start_port, end_port):
    print(f"\n🔎 Scanning {host} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"[+] Port {port} is OPEN")
        except KeyboardInterrupt:
            print("⛔ Scan stopped by user.")
            sys.exit()
        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    print("🛡️ porteye — Oddiy TCP port scanner")
    target = input("🎯 IP yoki domain manzil: ")
    try:
        start = int(input("🔢 Boshlanish port (masalan 20): "))
        end = int(input("🔢 Tugash port (masalan 1024): "))
        scan_ports(target, start, end)
    except ValueError:
        print("❗ Port raqamlarini to‘g‘ri kiriting.")
