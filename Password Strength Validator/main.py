import colorama
from colorama import Fore
from collections import Counter

colorama.init(autoreset=True)

MAX_SCORE = 12
BAR_WIDTH = 50

password = input(f"{Fore.LIGHTCYAN_EX}Please input your password: {Fore.RESET}")

score = 0


if not password.strip():
    percent = 0
    bar = "░" * BAR_WIDTH
    print(f"{Fore.RED}[{bar}] {percent}%  Very Weak{Fore.RESET}")
    raise SystemExit

length = len(password)


if length < 8:
    score += 0
elif 8 <= length <= 9:
    score += 2
elif 10 <= length <= 11:
    score += 3
elif 12 <= length <= 15:
    score += 4
elif 16 <= length <= 19:
    score += 5
else:  # 20+
    score += 6


has_lower = any(c.islower() for c in password)
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
has_symbol = any(not c.isalnum() for c in password)

score += 1 if has_lower else 0
score += 1 if has_upper else 0
score += 1 if has_digit else 0
score += 1 if has_symbol else 0


common_patterns = [
    "password", "qwerty", "admin", "letmein",
    "1234", "1111", "abcd"
]

pw_lower = password.lower()
if any(pattern in pw_lower for pattern in common_patterns):
    score -= 2

char_counts = Counter(password)
if max(char_counts.values()) >= 4:
    score -= 1


score = max(0, min(score, MAX_SCORE))


percent = round((score / MAX_SCORE) * 100)
filled = round((percent / 100) * BAR_WIDTH)
bar = "█" * filled + "░" * (BAR_WIDTH - filled)


if percent <= 24:
    label = "Very Weak"
    colour = Fore.RED
elif percent <= 49:
    label = "Weak"
    colour = Fore.RED
elif percent <= 74:
    label = "Medium"
    colour = Fore.YELLOW
elif percent <= 89:
    label = "Strong"
    colour = Fore.GREEN
else:
    label = "Very Strong"
    colour = Fore.GREEN

print(f"{colour}[{bar}] {percent}%  {label}{Fore.RESET}")


tips = []
if length < 12:
    tips.append("Use 12+ characters")
if not has_upper:
    tips.append("Add an uppercase letter")
if not has_digit:
    tips.append("Add a number")
if not has_symbol:
    tips.append("Add a symbol")
if any(pattern in pw_lower for pattern in common_patterns):
    tips.append("Avoid common words/patterns")
if max(char_counts.values()) >= 4:
    tips.append("Avoid repeating the same character")

if tips:
    print(f"{Fore.LIGHTBLACK_EX}Tips: " + " | ".join(tips) + Fore.RESET)
