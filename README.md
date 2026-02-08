# 🧰 Python CLI Tools

A growing collection of small, focused Python command-line projects built to practice and refine core programming fundamentals.

Each tool is intentionally kept simple, self-contained, and readable — prioritising clean logic, structure, and correctness over unnecessary complexity.

---

## ✨ About This Repository

This repository acts as a **learning sandbox** for experimenting with real application logic in Python.

Instead of one oversized project, it contains multiple mini tools. Each project focuses on a specific concept or combination of concepts, such as:

- user input & validation  
- control flow and state management  
- authentication and security basics  
- file-based persistence (JSON)  
- terminal UI design and menu systems  

Projects are added over time as new ideas or skills are explored.

---

## 📂 Repository Structure

- Each folder represents a **standalone CLI tool**
- Tools are designed to be run independently
- Completed projects are generally left stable rather than endlessly modified
- New tools build on lessons learned from earlier ones

---

## 🛠 Included Projects

### 📒 Notes & To-Do CLI (with Login System)
A fully featured, multi-user command-line application that combines authentication with personal productivity tools.

**Key features:**
- User registration and login
- Secure password hashing with salt
- Account lockout on repeated failures
- Per-user notes and tasks
- Add, view, delete notes
- Add, view, mark complete, delete tasks
- Persistent storage using JSON
- Menu-driven terminal interface

This project integrates a previously built login system directly into a larger tool, demonstrating how authentication and application logic can work together cleanly.

---

### 🏧 ATM System Simulation
A command-line simulation of a basic banking/ATM system.

**Focus areas:**
- Menu navigation
- Account state management
- Balance tracking
- Transaction-style logic

---

### 🔐 Login & Authentication Systems
Standalone experiments exploring authentication concepts.

**Focus areas:**
- Password hashing and salting
- Login validation
- Lockout logic
- File-based user storage

---

### 🔑 Password Strength Validator
A small utility that evaluates password strength based on length, patterns, repetition, and character variety.

**Focus areas:**
- String analysis
- Scoring systems
- Validation logic
- User feedback via terminal output

---

## 🚀 Getting Started

1. Clone the repository
2. Navigate into a project directory
3. Run the tool

Example:
```bash
cd notes_todo
python main.py
```

---

## 📌 Notes

- These projects are **learning-driven**, not production tools
- Code prioritises clarity and structure over clever tricks
- Concepts are intentionally repeated across projects to reinforce understanding

---

## 📈 Future Additions

More CLI tools will be added as new concepts are explored, including:
- extended stateful applications
- more advanced validation systems
- possible GUI or API-backed versions of existing tools
