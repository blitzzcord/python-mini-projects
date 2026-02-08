import json
import hashlib
import secrets
import os
import colorama
import sys
import time

from colorama import Fore

USERS_FILE = "./Login/users.json"  


# Helpers

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def slowprint(s, speed=0.03):
    for char in s:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Main functions

def load_users() -> dict:
    """Load users from JSON. If the file doesn't exist, return an empty dict."""
    os.makedirs("Login", exist_ok=True)
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_users(users: dict) -> None:
    """Save users to JSON."""
    os.makedirs("Login", exist_ok=True)
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)


def hash_password(password: str) -> tuple[str, str]:
    """
    Returns (password_hash, salt).
    - salt: random hex string
    - password_hash: sha256 of (password + salt), stored as hex string
    """
    salt = secrets.token_hex(16)
    combined = (password + salt).encode("utf-8")
    password_hash = hashlib.sha256(combined).hexdigest()
    return password_hash, salt

def verify_password(password: str, salt: str, stored_hash: str) -> bool:
    combined = (password + salt).encode("utf-8")
    computed_hash = hashlib.sha256(combined).hexdigest()
    return computed_hash == stored_hash


def main_menu():
    while True:
        clr()
        

        slowprint(f'{Fore.LIGHTYELLOW_EX}[ ✅ ] Login system{Fore.RESET}')
        time.sleep(1)

        choice = input(f'''
        {Fore.LIGHTYELLOW_EX}
        [1] Register
        [2] Login
        [3] Exit

        {Fore.RESET}''')
        
        if choice == "1":
            register()
        elif choice == "2":
            u = login()
            if u is not None:
                dashboard(u)
        elif choice == "3":
            sys.exit()
        else:
            clr()
            slowprint(f'{Fore.LIGHTYELLOW_EX}[ ❌ ] Invalid choice! {Fore.RESET}')
            time.sleep(0.5)
            continue

def dashboard(username):
    while True:
        clr()
        slowprint(f'{Fore.LIGHTYELLOW_EX}[ ✅ ] Logged in as {username}')
        time.sleep(1)

        choice = input(f'''
        {Fore.LIGHTYELLOW_EX}
        [1] Change Password
        [2] Logout
        [3] Exit

        {Fore.RESET}''')
        
        if choice == "1":
            change_password(username)
        elif choice == "2":
            slowprint(f'{Fore.GREEN}[ ✅ ] Logging out...{Fore.RESET}')
            time.sleep(0.2)
            return
        elif choice == "3":
            sys.exit()
        else:
            clr()
            slowprint(f'{Fore.LIGHTYELLOW_EX}[ ❌ ] Invalid choice! {Fore.RESET}')
            time.sleep(0.5)


def register():
    users = load_users()
    username = input(f'{Fore.LIGHTYELLOW_EX}Please enter a username: {Fore.RESET}')
    if not username.strip():
        print(f"{Fore.RED}[ ❌ ] Username cannot be empty.{Fore.RESET}")
        time.sleep(2)
        return
    
    elif username in users:
        print(f"[ ❌ ] Username is already in use.")
        time.sleep(2)
        return

    password = input(f'{Fore.LIGHTYELLOW_EX}Please enter a password: {Fore.RESET}')
    confirm = input(f'{Fore.LIGHTYELLOW_EX}Confirm your password: {Fore.RESET}')
    if not password.strip():
        print(f"{Fore.RED}[ ❌ ] Password cannot be empty.{Fore.RESET}")
    elif len(password) < 6:
        print(f"{Fore.RED}[ ❌ ] Password too short.{Fore.RESET}")
        time.sleep(2)
        return
    elif password != confirm:
        print(f'{Fore.RED}[ ❌ ] Passwords do not match!{Fore.RESET}')
        time.sleep(2)
        return
    else:
        pw_hash, salt = hash_password(password)
        users[username] = {
        "hash": pw_hash,
        "salt": salt,
        "failed": 0,
        "locked": False
    }
        save_users(users)
        print(f'{Fore.GREEN}[ ✅ ] Successfully created account, welcome {username}')
        time.sleep(2)
        return

    
def login():
    users = load_users()
    username = input(f'{Fore.LIGHTYELLOW_EX}Please enter your username: {Fore.RESET}').strip()

    if username not in users:
        print(f'{Fore.RED}[ ❌ ] Username not found!{Fore.RESET}')
        time.sleep(2)
        return None

    user = users[username]  

    if user["locked"]:
        print(f'{Fore.RED}[ ❌ ] Account locked!{Fore.RESET}')
        time.sleep(2)
        return None

    password = input(f'{Fore.LIGHTYELLOW_EX}Please enter a password: {Fore.RESET}')
    ok = verify_password(password, user["salt"], user["hash"])

    if ok:
        user["failed"] = 0
        users[username] = user
        save_users(users)  
        print(f'{Fore.GREEN}[ ✅ ] Successfully logged in!{Fore.RESET}')
        time.sleep(2)
        return username
    
    user["failed"] += 1

    if user["failed"] >= 3:
        user["locked"] = True
        print(f'{Fore.RED}[ ❌ ] Account locked!{Fore.RESET}')
    else:
        attempts_left = 3 - user["failed"]
        print(f'{Fore.RED}[ ❌ ] Incorrect password! {attempts_left} attempts left.{Fore.RESET}')

    users[username] = user
    save_users(users)
    time.sleep(2)
    return None

def change_password(username: str):
    users = load_users()
    user = users.get(username)

    if not user:
        print(f"{Fore.RED}[ ❌ ] User not found.{Fore.RESET}")
        time.sleep(2)
        return

    current_password = input(
        f"{Fore.LIGHTYELLOW_EX}Enter current password: {Fore.RESET}"
    )

    if not verify_password(current_password, user["salt"], user["hash"]):
        print(f"{Fore.RED}[ ❌ ] Incorrect current password.{Fore.RESET}")
        time.sleep(2)
        return

    new_password = input(
        f"{Fore.LIGHTYELLOW_EX}Enter new password: {Fore.RESET}"
    )
    confirm_password = input(
        f"{Fore.LIGHTYELLOW_EX}Confirm new password: {Fore.RESET}"
    )

    if not new_password.strip():
        print(f"{Fore.RED}[ ❌ ] Password cannot be empty.{Fore.RESET}")
        time.sleep(2)
        return

    if len(new_password) < 6:
        print(f"{Fore.RED}[ ❌ ] Password too short (min 6).{Fore.RESET}")
        time.sleep(2)
        return

    if new_password != confirm_password:
        print(f"{Fore.RED}[ ❌ ] Passwords do not match.{Fore.RESET}")
        time.sleep(2)
        return

    pw_hash, salt = hash_password(new_password) 
    user["hash"] = pw_hash
    user["salt"] = salt
    user["failed"] = 0
    user["locked"] = False

    users[username] = user
    save_users(users)

    print(f"{Fore.GREEN}[ ✅ ] Password changed successfully.{Fore.RESET}")
    time.sleep(2)
    return

main_menu()
