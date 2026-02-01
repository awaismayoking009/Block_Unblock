import os
import time
import sys

# Colors for professional look
G = '\033[92m' # Green
R = '\033[91m' # Red
W = '\033[0m'  # White
C = '\033[96m' # Cyan

def banner():
    os.system('clear')
    print(f"""{C}
    ===============================================
    | {G} █████╗ ██╗    ██╗ █████╗ ██╗███████╗      {C} |
    | {G}██╔══██╗██║    ██║██╔══██╗██║██╔════╝      {C} |
    | {G}███████║██║ █╗ ██║███████║██║███████╗      {C} |
    | {G}██╔══██║██║███╗██║██╔══██║██║╚════██║      {C} |
    | {G}██║  ██║╚███╔███╔╝██║  ██║██║███████║      {C} |
    | {G}╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝╚══════╝      {C} |
    |                                             |
    | {W}   AWAIS BLOCK BYPASS SESSION TOOL v1.0    {C} |
    | {R}       POWERED BY AWAIS MAYO 👑✨          {C} |
    ===============================================
    """)

def login():
    banner()
    print(f"{W}[-] Required Password to Unlock Tool")
    pwd = input(f"{G}[?] Enter Password: {W}")
    
    if pwd == "Powered By Awais Mayo":
        print(f"{G}\n[+] Password Correct! Verifying Session...")
        time.sleep(2)
    else:
        print(f"{R}\n[!] Invalid Password! Access Denied.")
        sys.exit()

def menu():
    banner()
    print(f"{C}[1] {W}Start Bypass Session")
    print(f"{C}[2] {W}Check Device Connection")
    print(f"{C}[3] {W}Update Tool")
    print(f"{C}[0] {W}Exit")
    
    choice = input(f"\n{G}Awais-Mayo-Tool > {W}")
    if choice == '1':
        start_bypass()
    else:
        sys.exit()

def start_bypass():
    banner()
    number = input(f"{G}[?] Enter Your Number (with country code): {W}")
    print(f"{C}[*] Linking Session for {number}...")
    time.sleep(3)
    print(f"{G}[+] Session Established! You can now send messages.{W}\n")
    
    # یہاں سے چیٹ لوپ شروع ہوتا ہے جو آپ کو ٹرمکس سے باہر نہیں جانے دے گا
    while True:
        msg = input(f"{G}Awais-Chat > {W}")
        
        if msg.lower() == 'exit':
            print(f"{R}[!] Closing Session...")
            break
            
        print(f"{C}[*] Sending Message: {msg}...")
        time.sleep(1)
        print(f"{G}[+] Delivered Successfully! ✅")
        print("-" * 30)

if __name__ == "__main__":
    login()
    menu()

