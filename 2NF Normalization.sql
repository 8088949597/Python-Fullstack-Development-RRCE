-- 2NF Example

-- Student Table
CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50)
);

-- Course Table
CREATE TABLE Course (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(50)
);

-- StudentCourse Junction Table
CREATE TABLE StudentCourse (
    student_id INT,
    course_id INT,
    PRIMARY KEY(student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- Insert Data into Student
INSERT INTO Student VALUES
(1, 'Kavya');

-- Insert Data into Course
INSERT INTO Course(course_name) VALUES
('Python'),
('Java');

-- Insert Data into StudentCourse
INSERT INTO StudentCourse VALUES
(1,1),
(1,2);

-- View Tables
SELECT * FROM Student;

SELECT * FROM Course;

SELECT * FROM StudentCourse;