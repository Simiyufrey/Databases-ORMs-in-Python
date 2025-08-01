from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):

    __tablename__ = 'Students'
    id = Column(Integer, primary_key = True , index = True)
    name = Column(String, nullable = False)
    age = Column(Integer, nullable =False)
    grade = Column(String, nullable = False)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age}, grade='{self.grade}')>" 