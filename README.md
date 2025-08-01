# Python Databases & ORMs Learning Series

## Overview
This repository is a step-by-step guide to mastering relational databases, SQL, and Object-Relational Mapping (ORM) in Python. You’ll start with raw SQL and SQLite, then move to advanced queries, and finally build a full-featured student record system using SQLAlchemy ORM.

---

## 📚 Lessons Breakdown

### Lesson 1: Introduction to Databases & SQL with SQLite
- What is a relational database?
- Introduction to SQLite (lightweight, file-based DB)
- Creating a database and table
- Basic SQL operations: CREATE, INSERT, SELECT, UPDATE, DELETE
- Querying with WHERE, ORDER BY, and LIMIT
- Using sqlite3 module in Python

**Exercise:**  
Create a Python script to:
- Create a `students.db`
- Create a `students` table
- Insert sample data and query it

---

### Lesson 2: Advanced SQL Queries and Joins
- Filtering with LIKE, IN, BETWEEN
- Aggregate functions: COUNT(), SUM(), AVG(), GROUP BY, HAVING
- Multi-table joins: INNER JOIN, LEFT JOIN
- Subqueries and views

**Exercise:**  
- Add a new table: `classes`
- Write SQL queries to fetch all students enrolled in a particular class
- Count the number of students in each class

---

### Lesson 3: Working with SQLite in Python
- Connecting to SQLite DB
- Executing SQL queries from Python
- Fetching data with `.fetchone()` and `.fetchall()`
- Using `?` parameter substitution (to prevent SQL injection)
- Transactions and committing changes

**Exercise:**  
Write a Python app to:
- Add new students
- List all students
- Delete a student by ID

---

### Lesson 4: Introduction to ORMs & SQLAlchemy
- What is an ORM?
- Installing SQLAlchemy
- Creating an engine, session, and base
- Defining models (tables) using Python classes
- Creating the database schema using `Base.metadata.create_all()`

**Exercise:**  
- Define Student and Class models using SQLAlchemy
- Initialize the database with sample data

---

### Lesson 5: CRUD Operations with SQLAlchemy
- Adding data with sessions
- Querying with `.query()`, `.filter()`, `.get()`
- Updating and deleting objects
- Handling exceptions (like IntegrityError)
- Committing and rolling back transactions

**Exercise:**  
Write CLI or script-based functions to:
- Create new student entries
- Update student data (e.g., name or class)
- Delete student by ID

---

### Lesson 6: Advanced SQLAlchemy – Relationships & Queries
- One-to-Many relationship: Class → Students
- Foreign keys and backrefs
- Querying with relationships (join, options)
- Using `like()`, `ilike()`, and filtering patterns
- Indexing, sorting, and paginating results

**Exercise:**  
- Link students to classes
- Query all students in a particular class
- Implement a search feature: find students by partial name

---

### Lesson 7: Project – Student Record System with Filters & Search
- Add/update/delete students
- List students (with pagination)
- Search by name/class
- Filter students by class or enrollment status
- Stretch: Add export to CSV
- Optional: Use Flask for a web interface

**Deliverable:**  
- Folder structure with `models.py`, `database.py`, and `main.py`
- Clear CLI or web-based interface for managing students
- Use SQLAlchemy throughout

---

## 📦 Technologies Used
- Python 3.10+
- SQLite (or PostgreSQL if scaling up)
- SQLAlchemy
- Optionally: Flask for web GUI

---

## 📁 Folder Structure
