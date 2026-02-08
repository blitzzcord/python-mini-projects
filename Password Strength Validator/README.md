# 🔐 Password Strength Validator (CLI)

A terminal-based password strength checker built in Python.  
It evaluates a user-provided password and displays a visual strength bar, percentage score, and feedback on how to improve the password.

This tool is designed for learning and experimentation, focusing on validation logic, scoring systems, and terminal UI output.

---

## ✨ Features

- Password strength scoring based on:
  - length
  - character variety (uppercase, lowercase, digits, symbols)
  - common weak patterns
  - repeated characters
- Visual **50-block strength bar**
- Percentage-based strength score
- Clear strength labels:
  - Very Weak
  - Weak
  - Medium
  - Strong
  - Very Strong
- Helpful improvement tips
- Coloured terminal output using `colorama`

---

## 📊 How It Works

Passwords are scored using a simple point-based system:

- **Length** contributes up to 6 points
- **Character variety** contributes up to 4 points
- **Penalties** reduce the score for:
  - common weak patterns (e.g. `password`, `1234`)
  - repeated characters

The final score is clamped and converted into a percentage, which is then rendered as a 50-character progress bar.

---

## ▶️ Running the Tool

1. Navigate to the project directory:
   ```bash
   cd password-validator
