from database import Base, engine, SessionLocal
from models import Student

# Step 1: Create database tables
Base.metadata.create_all(bind=engine)

# Step 2: Add sample students
def add_sample_students():
    session = SessionLocal()
    students = [
        Student(name="Amina Yusuf", age=17, grade="Form 3"),
        Student(name="Brian Otieno", age=16, grade="Form 2"),
        Student(name="Christine Mwangi", age=18, grade="Form 4"),
    ]
    session.add_all(students)
    session.commit()
    session.close()
    print("Sample students added!")

# Step 3: Run
if __name__ == "__main__":
    add_sample_students()
