-- Insert 5 Metro Stations

INSERT INTO Stations VALUES
(1, 'Majestic', 'Bangalore', 6, 2011),
(2, 'Indiranagar', 'Bangalore', 4, 2012),
(3, 'Whitefield', 'Bangalore', 5, 2020),
(4, 'MG Road', 'Bangalore', 3, 2010),
(5, 'Jayanagar', 'Bangalore', 4, 2015);

-- Insert 3 Metro Trains

INSERT INTO Trains VALUES
(101, 'Namma Metro A', 1000, 1),
(102, 'Namma Metro B', 1200, 2),
(103, 'Namma Metro C', 900, 3);

-- Update Capacity of One Train

UPDATE Trains
SET capacity = 1500
WHERE train_id = 102;

-- Delete One Station

DELETE FROM Stations
WHERE station_id = 5;

-- Display Stations

SELECT * FROM Stations;

-- Display Trains

SELECT * FROM Trains;