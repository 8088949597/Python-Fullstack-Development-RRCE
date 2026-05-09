-- Without Normalization

CREATE TABLE StudentCourse (
    student_id INT,
    student_name VARCHAR(50),
    course1 VARCHAR(50),
    course2 VARCHAR(50)
);

-- Example Data
INSERT INTO StudentCourse VALUES
(1, 'Kavya', 'Python', 'Java');

-- First Normal Form (1NF)

CREATE TABLE StudentCourse_1NF (
    student_id INT,
    student_name VARCHAR(50),
    course VARCHAR(50)
);

-- Example Data
INSERT INTO StudentCourse_1NF VALUES
(1, 'Kavya', 'Python'),
(1, 'Kavya', 'Java');