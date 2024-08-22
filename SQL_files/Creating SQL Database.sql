-- Creating the database

CREATE DATABASE IF NOT EXISTS BudgetBuddy; 

USE BudgetBuddy;

-- -----------------------------------------------

-- Creating the parent table; TRIPS. 
-- We used default values and triggers. 

CREATE TABLE Trips (
    trip_id INT AUTO_INCREMENT PRIMARY KEY,
    trip_name VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL
);

-- As this has a primary key, we need to insert values before creating the other tables.
-- This is why we have created the Duds and put defaults in place across the whole databse design.  

INSERT INTO Trips (trip_name, start_date)  VALUES
('Dud Trip', '2000-01-01');


-- Making sure the table has correctly been created. 
SELECT * FROM Trips;

-- -----------------------------------------------

-- Creating next table; Member_Details

CREATE TABLE Member_Details(
	member_id INT AUTO_INCREMENT PRIMARY KEY,
    member_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL
);

INSERT INTO Member_Details (member_name, email) VALUES
('Dud Dudson', 'dud@dudemail.com');

-- Making sure the table has correctly been created. 
SELECT * FROM Member_Details;

-- -----------------------------------------------

-- Creating next table; Costs

CREATE TABLE Costs(
	trip_id INT,
    flights_total FLOAT(10) DEFAULT 0 NOT NULL,
    accomodation_total FLOAT(10) DEFAULT 0 NOT NULL,
    transfers_total FLOAT(10) DEFAULT 0 NOT NULL,
    activities_total FLOAT(10) DEFAULT 0  NOT NULL,
    miscellaneous_total FLOAT(10) DEFAULT 0 NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES Trips(trip_id)
);

INSERT INTO Costs (trip_id)VALUES
('1');

-- Making sure the table has correctly been created. 
SELECT * FROM Costs;

-- -----------------------------------------------

-- Creating next table; Contributions 

CREATE TABLE Contributions(
	trip_id INT NOT NULL,
    member_id INT NOT NULL,
    total FLOAT(10) DEFAULT 0 NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES Trips(trip_id),
    FOREIGN KEY (member_id) REFERENCES Member_Details(member_id)
);

INSERT INTO Contributions (trip_id, member_id)VALUES
	('1','1');
    
    -- Making sure the table has correctly been created. 
SELECT * FROM Contributions;

-- -----------------------------------------------

-- Creating next table; Authentication 

CREATE TABLE Authentication(
username VARCHAR(50) PRIMARY KEY, 
member_id INT NOT NULL,
PWD VARBINARY(255),
FOREIGN KEY (member_id) REFERENCES Member_Details(member_id)
);

INSERT INTO Authentication (username, member_id, PWD)VALUES
	('thedud','1',md5('password'));
    

    -- Making sure the table has correctly been created. 
SELECT * FROM Authentication;

-- Testing that the password can be retrieved for the webapp. 
SELECT * FROM Authentication WHERE PWD=md5('password');