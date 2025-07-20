import database

def init():
    database.connect()

def add(name, roll, std_class, city):
    database.insert(name, roll, std_class, city)

def get_all():
    return database.fetch_all()

def update_record(student_id, name, roll, std_class, city):
    database.update(student_id, name, roll, std_class, city)

def delete_record(student_id):
    database.delete(student_id)
