-- Create Database
CREATE DATABASE FoodDeliveryDB;

-- Use Database
USE FoodDeliveryDB;

-- =========================
-- Create Customers Table
-- =========================
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50),
    phone VARCHAR(15)
);

-- =========================
-- Create Restaurants Table
-- =========================
CREATE TABLE Restaurants (
    restaurant_id INT PRIMARY KEY,
    restaurant_name VARCHAR(50),
    city VARCHAR(50),
    rating DECIMAL(2,1)
);

-- =========================
-- Create Food_Items Table
-- =========================
CREATE TABLE Food_Items (
    food_id INT PRIMARY KEY,
    food_name VARCHAR(50),
    price INT,
    restaurant_id INT,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(restaurant_id)
);

-- =========================
-- Create Orders Table
-- =========================
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    food_id INT,
    quantity INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (food_id) REFERENCES Food_Items(food_id)
);

-- =========================
-- Insert Data into Customers
-- =========================
INSERT INTO Customers VALUES
(1, 'Anu', 'Chennai', '9876543210'),
(2, 'Kavya', 'Bangalore', '9876541230'),
(3, 'Arjun', 'Hyderabad', '9876500000'),
(4, 'Rahul', 'Chennai', '9876512345');

-- =========================
-- Insert Data into Restaurants
-- =========================
INSERT INTO Restaurants VALUES
(1, 'Dominos', 'Chennai', 4.5),
(2, 'Pizza Hut', 'Bangalore', 4.2),
(3, 'KFC', 'Hyderabad', 4.0);

-- =========================
-- Insert Data into Food_Items
-- =========================
INSERT INTO Food_Items VALUES
(101, 'Veg Pizza', 250, 1),
(102, 'Chicken Burger', 180, 3),
(103, 'Paneer Pizza', 300, 2),
(104, 'French Fries', 120, 3),
(105, 'Cheese Pizza', 220, 2);

-- =========================
-- Insert Data into Orders
-- =========================
INSERT INTO Orders VALUES
(1, 1, 101, 2, '2026-05-01'),
(2, 2, 103, 1, '2026-05-02'),
(3, 3, 102, 3, '2026-05-03');

-- =========================
-- Task 1 : SELECT
-- Display all food items
-- =========================
SELECT * FROM Food_Items;

-- =========================
-- Task 2 : WHERE
-- Food items costing more than 200
-- =========================
SELECT * FROM Food_Items
WHERE price > 200;

-- =========================
-- Task 3 : AND / OR
-- =========================

-- Food items costing more than 150 and restaurant_id = 2
SELECT * FROM Food_Items
WHERE price > 150 AND restaurant_id = 2;

-- Restaurants in Chennai or Bangalore
SELECT * FROM Restaurants
WHERE city = 'Chennai' OR city = 'Bangalore';

-- =========================
-- Task 4 : LIKE
-- =========================

-- Customers whose names start with A
SELECT * FROM Customers
WHERE name LIKE 'A%';

-- Food items containing Pizza
SELECT * FROM Food_Items
WHERE food_name LIKE '%Pizza%';

-- =========================
-- Task 5 : BETWEEN
-- =========================

-- Food items price between 100 and 300
SELECT * FROM Food_Items
WHERE price BETWEEN 100 AND 300;

-- =========================
-- Task 6 : ORDER BY
-- =========================

-- Food items sorted by price descending
SELECT * FROM Food_Items
ORDER BY price DESC;
