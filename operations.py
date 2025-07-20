from db import connect

def add_student(name, roll, class_, city):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, roll, class, city) VALUES (?, ?, ?, ?)",
                   (name, roll, class_, city))
    conn.commit()
    conn.close()

def fetch_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    conn.close()
    return records

def update_student(id_, name, roll, class_, city):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=?, roll=?, class=?, city=? WHERE id=?",
                   (name, roll, class_, city, id_))
    conn.commit()
    conn.close()

def delete_student(id_):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id_,))
    conn.commit()
    conn.close()
