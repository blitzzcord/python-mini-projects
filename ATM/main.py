import os
import sys
import colorama 
from colorama import Fore
import msvcrt
import time

# ---------- HELPERS ---------- #

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def slowprint(s, speed=0.03):
    for char in s:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# ---------- VARIABLES ---------- #

balance = 0
cash = 0
pin = "2563"


# ---------- MENU ---------- #


def menu():
    clr()
    time.sleep(1)
    slowprint(f'{Fore.LIGHTYELLOW_EX}[ ✅ ] ATM system{Fore.RESET}')
    time.sleep(2)

    choice = input(f'''
    {Fore.LIGHTYELLOW_EX}
    [1] Deposit
    [2] Withdraw
    [3] Balance
    [4] Cash Add
    
    
                   
      {Fore.RESET}''')
    
    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        balance_view()
    elif choice == "4":
        cash_add()
    else:
        clr()
        slowprint(f'{Fore.LIGHTYELLOW_EX}[ ✅ ] Invalid choice! {Fore.RESET}')
        time.sleep(0.5)
        menu()

# ---------- FUNCTIONS ---------- #

def auth():
    clr()
    attempts_left = 3
    while attempts_left > 0:
        print(f'{Fore.LIGHTYELLOW_EX}[ ✅ ] Total attempts available: {attempts_left}')
        entered = input(f'{Fore.LIGHTYELLOW_EX}Enter PIN: {Fore.RESET}')
        if entered == pin:
            print(f'{Fore.GREEN}[ ✅ ] Successfully authenticated your pin{Fore.RESET}')
            time.sleep(2)
            return True
        else:
            attempts_left -= 1
            print(f'{Fore.RED} Inccorect pin! {attempts_left} attempts left.{Fore.RESET}')
            time.sleep(2)
            clr()
    clr()
    print(f'{Fore.RED}[ ❌ ] Card has been blocked, please contact the provider.{Fore.RESET}')
    time.sleep(3)
    sys.exit()


def cash_add():
    global cash
    amount_to_add = int(input(f'{Fore.LIGHTYELLOW_EX}Amount to add to cash variable: ${Fore.RESET}'))
    cash += amount_to_add
    print(f'{Fore.LIGHTYELLOW_EX}[ ✅ ] Successfully added ${amount_to_add} to your available cash')
    time.sleep(3)
    menu()

def deposit():
    global cash, balance
    clr()
    amount_to_deposit = int(input(f'{Fore.LIGHTYELLOW_EX}How much cash would you like to deposit: ${Fore.RESET}'))
    if amount_to_deposit > cash:
        print(f'{Fore.LIGHTYELLOW_EX}[ ✅ ] Insufficient funds.')
        time.sleep(3)
        menu()
    else:
        balance += amount_to_deposit
        cash -= amount_to_deposit
        print(f'{Fore.LIGHTYELLOW_EX}[ ✅ ] Successfully deposited ${amount_to_deposit} to your account.{Fore.RESET}')
        time.sleep(3)
        menu()

def withdraw():
    global cash, balance
    clr()
    amount_to_withdraw = int(input(f'{Fore.LIGHTYELLOW_EX}How much cash would you like to withdraw: ${Fore.RESET}'))
    if amount_to_withdraw > balance:
        print(f'{Fore.LIGHTYELLOW_EX}[ ✅ ] Insufficient funds in account')
        time.sleep(3)
        menu()
    else:
        balance -= amount_to_withdraw
        cash += amount_to_withdraw
        print(f'{Fore.LIGHTYELLOW_EX}[ ✅ ] Successfully withdrew ${amount_to_withdraw} from your account. {Fore.RESET}')
        time.sleep(3)
        menu()

def balance_view():
    clr()
    print(f'''
    {Fore.LIGHTYELLOW_EX}
    [ ✅ ] Cash: ${cash}
    [ ✅ ] Balance: ${balance}
          
          {Fore.RESET}''')
    slowprint(f"{Fore.LIGHTYELLOW_EX}Press any key to continue...{Fore.RESET}")
    msvcrt.getch()
    menu()
    
# ---------- RUN ---------- #
if auth() == True:
    menu()

