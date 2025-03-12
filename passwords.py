import os
import platform
import socket
import subprocess
import hashlib
import base64


def wifi_passwords():
    print("\n[+] Saved Wi-Fi Passwords:")
    command = "netsh wlan show profiles"
    networks = subprocess.run(command, shell=True, capture_output=True, text=True).stdout
    profiles = [line.split(":")[1].strip() for line in networks.split("\n") if "All User Profile" in line]

    for profile in profiles:
        command = f'netsh wlan show profile "{profile}" key=clear'
        results = subprocess.run(command, shell=True, capture_output=True, text=True).stdout
        for line in results.split("\n"):
            if "Key Content" in line:
                print(f"{profile}: {line.split(':')[1].strip()}")

def main():
    while True:
        print("\n[+] Python Multi-Tool")
        print("1. System Info")
        print("2. Network Scan")
        print("3. List Processes")
        print("4. Encrypt Text")
        print("5. Decrypt Text")
        print("6. View Wi-Fi Passwords")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            system_info()
        elif choice == "2":
            target = input("Enter IP to scan: ")
            network_scan(target)
        elif choice == "3":
            list_processes()
        elif choice == "4":
            text = input("Enter text to encrypt: ")
            encrypt_text(text)
        elif choice == "5":
            text = input("Enter text to decrypt: ")
            decrypt_text(text)
        elif choice == "6":
            wifi_passwords()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
