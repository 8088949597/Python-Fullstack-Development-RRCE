-- Create Database
CREATE DATABASE MetroDB;

-- Use Database
USE MetroDB;

-- Create Stations Table
CREATE TABLE Stations (
    station_id INT PRIMARY KEY,
    station_name VARCHAR(50),
    location VARCHAR(50),
    platforms INT
);

-- Create Metro_Trains Table
CREATE TABLE Metro_Trains (
    train_id INT PRIMARY KEY,
    train_name VARCHAR(50),
    capacity INT,
    station_id INT,
    FOREIGN KEY (station_id) REFERENCES Stations(station_id)
);

-- Add New Column to Stations
ALTER TABLE Stations
ADD opening_year INT;

-- Rename Table
RENAME TABLE Metro_Trains TO Trains;