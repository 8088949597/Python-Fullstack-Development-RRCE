-- Create Database
CREATE DATABASE universityDB;

-- Use Database
USE universityDB;

-- Create Students Table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    marks INT,
    attendance INT
);

-- Insert 10 Student Records
INSERT INTO students VALUES
(1, 'Rahul', 'CSE', 92, 90),
(2, 'Priya', 'ECE', 85, 88),
(3, 'Amit', 'MECH', 76, 82),
(4, 'Neha', 'CSE', 95, 91),
(5, 'Kiran', 'EEE', 67, 79),
(6, 'Sneha', 'ECE', 89, 87),
(7, 'Arjun', 'CIVIL', 81, 84),
(8, 'Pooja', 'CSE', 78, 92),
(9, 'Vikram', 'MECH', 90, 89),
(10, 'Anjali', 'ECE', 83, 86);

-- Display All Students
SELECT * FROM students;

-- Create View for Eligible Scholarship Students
CREATE VIEW eligible_scholarship_students AS
SELECT *
FROM students
WHERE marks > 80
AND attendance > 85
WITH CHECK OPTION;

-- Display Eligible Students Using View
SELECT * FROM eligible_scholarship_students;

-- Try to Insert Invalid Student Through View
INSERT INTO eligible_scholarship_students
VALUES (11, 'Ramesh', 'CSE', 70, 90);

-- Display View Again
SELECT * FROM eligible_scholarship_students;

-- Display Original Table
SELECT * FROM students;