import sqlite3

def connect():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll TEXT,
            class TEXT,
            city TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert(name, roll, std_class, city):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO student (name, roll, class, city) VALUES (?, ?, ?, ?)",
                (name, roll, std_class, city))
    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    conn.close()
    return rows

def update(student_id, name, roll, std_class, city):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("UPDATE student SET name=?, roll=?, class=?, city=? WHERE id=?",
                (name, roll, std_class, city, student_id))
    conn.commit()
    conn.close()

def delete(student_id):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (student_id,))
    conn.commit()
    conn.close()
