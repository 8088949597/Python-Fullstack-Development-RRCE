-- Create Database
CREATE DATABASE hospitalDB;

-- Use Database
USE hospitalDB;

-- Create Doctors Table
CREATE TABLE Doctors (
    doctor_id INT PRIMARY KEY,
    doctor_name VARCHAR(50),
    specialization VARCHAR(50),
    max_patients_per_day INT,
    booked_patients INT
);

-- Create Patients Table
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY,
    patient_name VARCHAR(50)
);

-- Create Appointments Table
CREATE TABLE Appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

-- Insert Sample Doctors
INSERT INTO Doctors VALUES
(1, 'Dr. Sharma', 'Cardiology', 2, 1),
(2, 'Dr. Mehta', 'Neurology', 3, 3),
(3, 'Dr. Reddy', 'Orthopedic', 4, 2),
(4, 'Dr. Khan', 'Dermatology', 2, 0),
(5, 'Dr. Priya', 'Pediatrics', 5, 4);

-- Insert Sample Patients
INSERT INTO Patients VALUES
(1, 'Rahul'),
(2, 'Sneha'),
(3, 'Amit'),
(4, 'Pooja'),
(5, 'Kiran'),
(6, 'Neha'),
(7, 'Arjun'),
(8, 'Anjali'),
(9, 'Vikram'),
(10, 'Priya');

-- Create Stored Procedure
DELIMITER //

CREATE PROCEDURE book_appointment(
    IN p_patient_id INT,
    IN p_doctor_id INT,
    IN p_appointment_date DATE
)
BEGIN
    DECLARE max_slots INT;
    DECLARE booked_slots INT;

    -- Get doctor slot details
    SELECT max_patients_per_day, booked_patients
    INTO max_slots, booked_slots
    FROM Doctors
    WHERE doctor_id = p_doctor_id;

    -- Check availability
    IF booked_slots < max_slots THEN

        -- Insert appointment
        INSERT INTO Appointments(patient_id, doctor_id, appointment_date)
        VALUES (p_patient_id, p_doctor_id, p_appointment_date);

        -- Update booked patients count
        UPDATE Doctors
        SET booked_patients = booked_patients + 1
        WHERE doctor_id = p_doctor_id;

        -- Success Message
        SELECT 'Appointment Booked Successfully' AS Message;

    ELSE

        -- Doctor Full Message
        SELECT 'Doctor not available today' AS Message;

    END IF;

END //

DELIMITER ;

-- Task 4: Call Procedure (Doctor has slots available)
CALL book_appointment(3,1,'2026-03-15');

-- Task 5: Test Doctor Full Situation
CALL book_appointment(4,2,'2026-03-15');

-- Display Appointments
SELECT * FROM Appointments;

-- Display Doctors Table
SELECT * FROM Doctors;
