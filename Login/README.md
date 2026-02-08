# 🔐 Login System (CLI)

A terminal-based login and authentication system built in Python to practice core concepts such as user validation, password hashing, state management, and file-based persistence.

This project is part of the **Python CLI Tools** repository and is intended for learning purposes.

---

## ✨ Features

- User registration
- Secure password hashing with salt
- Login authentication
- Account lockout after failed attempts
- Change password while logged in
- Persistent user storage using JSON
- Simple, menu-driven terminal interface
- Coloured terminal output using `colorama`

---

## 📂 How It Works

- User data is stored locally in a JSON file
- Passwords are **never stored in plain text**
- Each user has:
  - a unique salt
  - a hashed password
  - failed login counter
  - lock status
- A dashboard is shown after successful login

---

## ▶️ Running the Program

1. Navigate to the login folder:
   ```bash
   cd login
