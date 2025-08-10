# py_CRUD

A simple Python-based CRUD (Create, Read, Update, Delete) application for managing student records using SQLite.

## 📌 Features
- Add new student records
- View all student details
- Update existing student information
- Delete student records
- Data stored locally in `students.db` (SQLite)

## 🛠️ Tech Stack
- **Language:** Python
- **Database:** SQLite
- **Modules Used:** `sqlite3`, `tkinter` (for GUI, if applicable)

## 📂 Project Structure
├── database.py           # Handles database connection and table creation
├── main.py               # Entry point for the application 
├── student_form.py       # GUI form for adding/updating students 
├── student_operations.py # CRUD operations 
├── students.db           # SQLite database file 
└── pycache/          # Compiled Python files
