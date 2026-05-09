-- =========================
-- 1. INNER JOIN
-- =========================

-- Create Students Table
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50)
);

-- Create Clubs Table
CREATE TABLE Clubs (
    club_id INT PRIMARY KEY,
    club_name VARCHAR(50)
);

-- Create Student_Club Table
CREATE TABLE Student_Club (
    student_id INT,
    club_id INT
);

-- Insert Data into Students
INSERT INTO Students VALUES
(1, 'Rahul'),
(2, 'Priya'),
(3, 'Amit'),
(4, 'Neha');

-- Insert Data into Clubs
INSERT INTO Clubs VALUES
(101, 'Robotics'),
(102, 'Photography');

-- Insert Data into Student_Club
INSERT INTO Student_Club VALUES
(1, 101),
(2, 102),
(3, 101);

-- INNER JOIN Query
SELECT Students.name, Clubs.club_name
FROM Students
INNER JOIN Student_Club
ON Students.student_id = Student_Club.student_id
INNER JOIN Clubs
ON Student_Club.club_id = Clubs.club_id;


-- =========================
-- 2. LEFT JOIN
-- =========================

-- Create Users Table
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    name VARCHAR(50)
);

-- Create Subscriptions Table
CREATE TABLE Subscriptions (
    sub_id INT PRIMARY KEY,
    user_id INT,
    plan VARCHAR(50)
);

-- Insert Data into Users
INSERT INTO Users VALUES
(1, 'Arjun'),
(2, 'Sneha'),
(3, 'Karan'),
(4, 'Meera');

-- Insert Data into Subscriptions
INSERT INTO Subscriptions VALUES
(201, 1, 'Premium'),
(202, 2, 'Basic');

-- LEFT JOIN Query
SELECT Users.name, Subscriptions.plan
FROM Users
LEFT JOIN Subscriptions
ON Users.user_id = Subscriptions.user_id;


-- =========================
-- 3. RIGHT JOIN
-- =========================

-- Create Authors Table
CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(50)
);

-- Create Books Table
CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(50),
    author_id INT
);

-- Insert Data into Authors
INSERT INTO Authors VALUES
(1, 'R.K. Narayan'),
(2, 'Chetan Bhagat');

-- Insert Data into Books
INSERT INTO Books VALUES
(301, 'Malgudi Days', 1),
(302, 'Five Point Someone', 2),
(303, 'Unknown Mystery', NULL);

-- RIGHT JOIN Query
SELECT Books.title, Authors.author_name
FROM Authors
RIGHT JOIN Books
ON Authors.author_id = Books.author_id;