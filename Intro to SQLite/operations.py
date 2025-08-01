import sqlite3

DB_NAME = 'student_records.db'

def view_all_students():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def add_student(name, age, grade,gender):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (name, age, grade,gender)
        VALUES (?, ?, ?,?)
    ''', (name, age, grade,gender))
    conn.commit()
    conn.close()
    print(f"Added: {name}")

def update_student(student_id, name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE students
        SET name = ?
        WHERE id = ?
    ''', (name, student_id))
    conn.commit()
    conn.close()
    print(f"Updated student ID {student_id} to {name}")

def delete_student(student_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    print(f"Deleted student ID {student_id}")

# Test functions
if __name__ == '__main__':
    print("All students:")
    view_all_students()

    print("\nAdding student...")
    add_student("Fatuma Ali", 17, "Form 3","F")

    print("\nAfter addition:")
    view_all_students()

    print("\nUpdating student ID 1...")
    update_student(1, "Amina Yusuf Hassan")

    print("\nAfter update:")
    view_all_students()

    print("\nDeleting student ID 2...")
    delete_student(2)

    print("\nFinal list:")
    view_all_students()
