# 🗒️ Notes & To-Do CLI (with User Accounts)

A terminal-based **Notes & To-Do application** written in Python that features a **fully integrated login system**, user-specific data storage, and clean menu navigation.

This project combines multiple mini-systems into one cohesive CLI tool:
- Secure user authentication
- Per-user notes
- Per-user to-do lists
- Persistent JSON storage
- Structured menus for smooth navigation

---

## ✨ Key Features

### 🔐 User Authentication System
- Register and login with usernames and passwords
- Passwords are securely hashed with a unique salt (SHA-256)
- Accounts are locked after multiple failed login attempts
- Passwords can be changed while logged in

The login system acts as the **entry point** to the entire application, ensuring every note and task is tied to a specific user.

---

### 🧭 Menu-Driven Interface
The application is built around **layered menus** that flow naturally:

- **Main Menu**
  - Register
  - Login
  - Exit

- **User Dashboard**
  - Notes
  - To-Do
  - Change Password
  - Logout

- **Notes Menu**
  - Add notes
  - View notes
  - Delete notes by ID

- **To-Do Menu**
  - Add tasks
  - View tasks
  - Mark tasks as complete
  - Delete tasks by ID

Each menu loops cleanly and returns the user to the correct level, making the app feel structured and intuitive despite running entirely in the terminal.

---

### 📝 Notes System
- Notes are created with:
  - Unique incremental IDs
  - Timestamps
  - User ownership
- Notes are stored per-user
- Notes can be viewed or deleted safely by ID

---

### ✅ To-Do System
- Tasks include:
  - Unique IDs
  - Completion status (`done: true/false`)
  - Creation timestamps
- Tasks are tied to the logged-in user
- Tasks can be:
  - Added
  - Viewed with visual status indicators (✅ / ❌)
  - Marked as complete
  - Deleted by ID

---

### 💾 Persistent Data Storage
All data is stored in JSON files:
- `users.json` → login credentials & security data
- `user_data.json` → notes and tasks per user

Data is automatically loaded and saved, allowing users to close and reopen the program without losing progress.

---

## 🧠 How the Login System Fits Everything Together

The login system is the **core controller** of the app:

1. A user logs in
2. Their username becomes the active session identity
3. Every menu, note, and task function receives this username
4. All actions read/write data **only for that user**

This design ensures:
- No data overlap between users
- Clean separation of authentication and features
- Easy expansion (new tools can plug into the same system)

---

## 🛠️ Technologies Used
- Python 3
- JSON for persistence
- `hashlib` + `secrets` for password security
- `colorama` for colored CLI output
- `datetime` for timestamps

---

## 🚀 Why This Project Matters
This project demonstrates:
- Real authentication logic
- Stateful CLI applications
- CRUD operations
- Data persistence
- Clean program flow using menus
- Scalable structure for adding new tools

It’s designed to grow — more features can be added without rewriting the core system.

---

## 📌 Future Ideas
- Edit notes / tasks
- Filter tasks (completed vs pending)
- Export notes/tasks
- Session activity logs
- Encrypted data storage

---

## 🧑‍💻 Author
Built as part of a growing collection of Python CLI tools focused on **learning real application structure**, not just scripts.

---

