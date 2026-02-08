import json
import hashlib
import secrets
import os
import colorama
from datetime import datetime
import sys
import time

from colorama import Fore

USERS_FILE = "./Notes_todo/data/users.json"  
DATA_FILE = "./Notes_todo/data/user_data.json"


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
    os.makedirs("./Notes_todo/data", exist_ok=True)
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_users(users: dict) -> None:
    """Save users to JSON."""
    os.makedirs("./Notes_todo/data", exist_ok=True)
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

def load_data() -> dict:
    """Load users from JSON. If the file doesn't exist, return an empty dict."""
    os.makedirs("data", exist_ok=True)
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
def ensure_user_data(data, username):
    if username not in data:
        data[username] = {
            "notes": [],
            "tasks": []
        }
    return data[username]


def save_data(data: dict) -> None:
    """Save users to JSON."""
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


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
        [1] Notes
        [2] To-Do
        [3] Change Password
        [4] Logout

        {Fore.RESET}''')
        
        if choice == "1":
            notes_menu(username)
        elif choice == "2":
            to_do_menu(username)
        elif choice == "3":
            change_password(username)
        elif choice == "4":
            slowprint(f'{Fore.GREEN}[ ✅ ] Logging out...{Fore.RESET}')
            time.sleep(0.2)
            return
        else:
            clr()
            slowprint(f'{Fore.LIGHTYELLOW_EX}[ ❌ ] Invalid choice! {Fore.RESET}')
            time.sleep(0.5)

def notes_menu(username):
    while True:
        clr()
        slowprint(f'{Fore.LIGHTYELLOW_EX}[ ✅ ] Logged in as {username}')
        time.sleep(1)

        choice = input(f'''
        {Fore.LIGHTYELLOW_EX}
    [>] Notes menu
        
        [1] Add Note
        [2] View Notes
        [3] Delete Note (by id)
        [4] Back

        {Fore.RESET}''')
        
        if choice == "1":
            add_note(username)
        elif choice == "2":
            view_notes(username)
        elif choice == "3":
            delete_note(username)
        elif choice == "4":
            time.sleep(0.2)
            return
        else:
            clr()
            slowprint(f'{Fore.LIGHTYELLOW_EX}[ ❌ ] Invalid choice! {Fore.RESET}')
            time.sleep(0.5)

def to_do_menu(username):
    while True:
        clr()
        slowprint(f'{Fore.LIGHTYELLOW_EX}[ ✅ ] Logged in as {username}')
        time.sleep(1)

        choice = input(f'''
        {Fore.LIGHTYELLOW_EX}

    [>] Task menu
        
        [1] Add Task
        [2] View Tasks
        [3] Mark done (by id)
        [4] Delete Task (by id)
        [5] Back

        {Fore.RESET}''')
        
        if choice == "1":
            add_task(username)
        elif choice == "2":
            view_tasks(username)
        elif choice == "3":
            mark_task_done(username)
        elif choice == "4":
            delete_task(username)
        elif choice == "5":
            return
        else:
            clr()
            slowprint(f'{Fore.LIGHTYELLOW_EX}[ ❌ ] Invalid choice! {Fore.RESET}')
            time.sleep(0.5)


def register():
    users = load_users()
    username = input(f'{Fore.LIGHTYELLOW_EX}Please enter a username: {Fore.RESET}')
    username = username.strip().lower()
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
    username = username.strip().lower()

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

def add_note(username):
    data = load_data()
    user_data = ensure_user_data(data, username)

    note_text = input(f"{Fore.LIGHTCYAN_EX}Enter your note: {Fore.RESET}").strip()
    if not note_text:
        print(f"{Fore.RED}[ ❌ ] Note cannot be empty.{Fore.RESET}")
        time.sleep(1.5)
        return

    # Generate next ID
    if not user_data["notes"]:
        next_id = 1
    else:
        next_id = max(note["id"] for note in user_data["notes"]) + 1

    new_note = {
        "id": next_id,
        "text": note_text,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    user_data["notes"].append(new_note)
    save_data(data)

    print(f"{Fore.GREEN}[ ✅ ] Note added successfully.{Fore.RESET}")
    time.sleep(1.5)
    return

def view_notes(username):
    data = load_data()
    user_data = ensure_user_data(data, username)

    if not user_data["notes"]:
        print(f"{Fore.RED}[ ❌ ] You have no current notes.{Fore.RESET}")
        time.sleep(1.5)
        return

    print(f"{Fore.LIGHTCYAN_EX}\nYour notes:\n{Fore.RESET}")

    for note in user_data["notes"]:
        print(
            f"{Fore.YELLOW}[{note['id']}] "
            f"{note['text']} "
            f"{Fore.WHITE}({note['created']})"
        )

    input(f"\n{Fore.LIGHTCYAN_EX}Press Enter to return...{Fore.RESET}")

def delete_note(username):
    data = load_data()
    user_data = ensure_user_data(data, username)

    raw = input(f"{Fore.LIGHTCYAN_EX}Enter your note id: {Fore.RESET}").strip()
    if not raw:
        print(f"{Fore.RED}[ ❌ ] Note id cannot be empty.{Fore.RESET}")
        time.sleep(1.5)
        return
    if not raw.isdigit():
        print(f"{Fore.RED}[ ❌ ] Note id must be a number.{Fore.RESET}")
        time.sleep(1.5)
        return

    note_id = int(raw)

    ids = [note["id"] for note in user_data["notes"]]
    if note_id not in ids:
        print(f"{Fore.RED}[ ❌ ] Note not found.{Fore.RESET}")
        time.sleep(1.5)
        return

    user_data["notes"] = [note for note in user_data["notes"] if note["id"] != note_id]
    save_data(data)

    print(f"{Fore.GREEN}[ ✅ ] Note deleted successfully.{Fore.RESET}")
    time.sleep(1.5)



def add_task(username):
    data = load_data()
    user_data = ensure_user_data(data, username)

    task_name = input(f"{Fore.LIGHTCYAN_EX}Enter your task name: {Fore.RESET}").strip()
    if not task_name:
        print(f"{Fore.RED}[ ❌ ] Task cannot be empty.{Fore.RESET}")
        time.sleep(1.5)
        return

    
    if not user_data["tasks"]:
        next_id = 1
    else:
        next_id = max(task["id"] for task in user_data["tasks"]) + 1

    new_task = {
        "id": next_id,
        "text": task_name,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    user_data["tasks"].append(new_task)
    save_data(data)

    print(f"{Fore.GREEN}[ ✅ ] Task added successfully.{Fore.RESET}")
    time.sleep(1.5)
    return

def view_tasks(username):
    data = load_data()
    user_data = ensure_user_data(data, username)

    if not user_data["tasks"]:
        print(f"{Fore.RED}[ ❌ ] You have no current tasks.{Fore.RESET}")
        time.sleep(1.5)
        return

    print(f"{Fore.LIGHTCYAN_EX}\nYour tasks:\n{Fore.RESET}")

    for task in user_data["tasks"]:
        status = "✅" if task["done"] else "❌"

        print(
            f"{Fore.YELLOW}[{task['id']}] "
            f"{status} {task['text']} "
            f"{Fore.WHITE}({task['created']})"
        )

    input(f"\n{Fore.LIGHTCYAN_EX}Press Enter to return...{Fore.RESET}")

def mark_task_done(username):
    data = load_data()
    user_data = ensure_user_data(data, username)

    raw = input(f"{Fore.LIGHTCYAN_EX}Enter your task id: {Fore.RESET}").strip()
    if not raw:
        print(f"{Fore.RED}[ ❌ ] Task id cannot be empty.{Fore.RESET}")
        time.sleep(1.5)
        return
    if not raw.isdigit():
        print(f"{Fore.RED}[ ❌ ] Task id must be a number.{Fore.RESET}")
        time.sleep(1.5)
        return

    task_id = int(raw)

    ids = [task["id"] for task in user_data["tasks"]]
    if task_id not in ids:
        print(f"{Fore.RED}[ ❌ ] Task not found.{Fore.RESET}")
        time.sleep(1.5)
        return

    for task in user_data["tasks"]:
        if task["id"] == task_id:
            if task["done"]:
                print(f"{Fore.YELLOW}[ ✅ ] Task is already marked as done.{Fore.RESET}")
                time.sleep(1.5)
                return
            task["done"] = True
            break
    save_data(data)

    print(f"{Fore.GREEN}[ ✅ ] Task marked as completed!{Fore.RESET}")
    time.sleep(1.5)

def delete_task(username):
    data = load_data()
    user_data = ensure_user_data(data, username)

    raw = input(f"{Fore.LIGHTCYAN_EX}Enter your task id: {Fore.RESET}").strip()
    if not raw:
        print(f"{Fore.RED}[ ❌ ] Task id cannot be empty.{Fore.RESET}")
        time.sleep(1.5)
        return
    if not raw.isdigit():
        print(f"{Fore.RED}[ ❌ ] Task id must be a number.{Fore.RESET}")
        time.sleep(1.5)
        return

    task_id = int(raw)

    ids = [task["id"] for task in user_data["tasks"]]
    if task_id not in ids:
        print(f"{Fore.RED}[ ❌ ] Task not found.{Fore.RESET}")
        time.sleep(1.5)
        return

    user_data["tasks"] = [task for task in user_data["tasks"] if task["id"] != task_id]
    save_data(data)

    print(f"{Fore.GREEN}[ ✅ ] Task deleted successfully.{Fore.RESET}")
    time.sleep(1.5)


main_menu()
