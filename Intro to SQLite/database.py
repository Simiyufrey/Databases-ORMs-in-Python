import sqlite3

# Connect to SQLite DB (or create if not exists)
conn = sqlite3.connect("student_records.db")

cursor = conn.cursor()

# Create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL,
    gender TEXT NOT NULL
)
''')



# Insert sample students
students = [
    ('Amina Yusuf', 17, 'Form 3', 'F'),
    ('Brian Otieno', 16, 'Form 2','M'),
    ('Christine Mwangi', 18, 'Form 4','F'),
]


cursor.executemany('''
INSERT INTO students (name, age, grade,gender)
VALUES (?, ?, ?,?)
''', students)

# Commit changes and close

print("record saved successfully")
conn.commit()
conn.close()

