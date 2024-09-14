#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 09:55:27 2024

@author: matt
"""
#%%
!pip install sqlalchemy
import sqlite3
from pathlib import Path
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
!pip install ipython-sql
#%%
conn = sqlite3.connect("student_grades.db")
c = conn.cursor()
#%%
c.execute(
     """
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);
""")
#%%
c.execute(
   """
CREATE TABLE grades (
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
""")
#%%
students = [
    ('Alice', 'Johnson'),
    ('Bob', 'Smith'),
    ('Carol', 'White'),
    ('David', 'Brown'),
    ('Eve', 'Davis')
]
c.executemany("""
    INSERT INTO students (first_name, last_name) 
    VALUES (?, ?)""", students)
#%%
student_grades = [
    (1, 1, 'Math', 95),
    (2, 1, 'English', 88),
    (3, 1, 'History', 90),
    (4, 2, 'Math', 82),
    (5, 2, 'English', 76),
    (6, 2, 'History', 85),
    (7, 3, 'Math', 89),
    (8, 3, 'English', 93),
    (9, 3, 'History', 98),
    (10, 4, 'Math', 97),
    (11, 4, 'English', 95),
    (12, 4, 'History', 98),
    (13, 5, 'Math', 83),
    (14, 5, 'English', 86),
    (15, 5, 'History', 84)
]

c.executemany(
    """
    INSERT INTO grades (grade_id, student_id, subject, grade) VALUES (?, ?, ?, ?)
    """,
    student_grades
)
#%%
""" 1) Retrieve all students' names and their grades """
student_grades = """
    SELECT students.first_name, students.last_name, grades.subject, grades.grade
    FROM students
    JOIN grades ON students.student_id = grades.student_id;
    """
c.execute(student_grades)
results = c.fetchall()
print(results)
#%%
""" 2) Find the average grade for each student """
student_avg_grade = """
    SELECT students.first_name, students.last_name, AVG(grades.grade) AS average_grade
    FROM students
    JOIN grades ON students.student_id = grades.student_id
    GROUP BY students.first_name, students.last_name
    """
c.execute(student_avg_grade)
results1 = c.fetchall()
print(results1)
#%%
""" 3) Find the student with the highest average grade """
highest_avg = """
    SELECT students.first_name, students.last_name, AVG(grades.grade) AS average_grade
    FROM students
    JOIN grades ON students.student_id = grades.student_id
    GROUP BY first_name, last_name
    ORDER BY average_grade DESC
    LIMIT 1;
    """
c.execute(highest_avg)
results2 = c.fetchall()
print(results2)
#%%
""" 4) Find the average grade for the Math subject """
math_avg = """
    SELECT AVG(grades.grade) AS avg_math_grade
    FROM grades
    WHERE subject = "Math"
    """
c.execute(math_avg)
results3 = c.fetchall()
print(results3)
#%%
""" 5) List all students who scored above 90 in any subject """
above90 = """
    SELECT DISTINCT students.first_name, students.last_name, grades.grade
    FROM students
    JOIN grades ON students.student_id = grades.student_id
    WHERE grades.grade > 90
    """
c.execute(above90)
results4 = c.fetchall()
print(results4)

#%%
students_df = pd.read_sql_query("SELECT * FROM students", conn)
grades_df = pd.read_sql_query("SELECT * FROM grades", conn)
#%%
Master_DataFrame = pd.read_sql_query("""
    WITH AverageGrades AS (
    SELECT student_id, AVG(grade) AS avg_grade
    FROM grades
    GROUP BY student_id
)
SELECT first_name, last_name, subject, grade, avg_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN AverageGrades ag ON s.student_id = ag.student_id
""", conn)

#%%
avggradedf = Master_DataFrame[['first_name', 'avg_grade']].drop_duplicates()
plt.scatter(avggradedf['first_name'], avggradedf['avg_grade'])
plt.bar(avggradedf['first_name'], avggradedf['avg_grade'])
