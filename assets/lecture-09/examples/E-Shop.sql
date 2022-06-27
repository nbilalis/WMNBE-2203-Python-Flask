-- CREATE DATABASE `E-Shop`;

-- USE `E-Shop`;

-- BEGIN TRANSACTION;

DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS ProductCategories;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS CustomerCredentials;
DROP TABLE IF EXISTS Addresses;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS OrderItems;

CREATE TABLE Products (
	Id INTEGER PRIMARY KEY AUTOINCREMENT,
	Title VARCHAR(50) NOT NULL,
	Description VARCHAR(250) NOT NULL,
	LongDescription TEXT NOT NULL,
	Price DECIMAL(6,2) NOT NULL,
	Stock INTEGER NOT NULL
);

ALTER TABLE Products DROP COLUMN Stock;
ALTER TABLE Products ADD COLUMN Stock INTEGER DEFAULT(0);

CREATE TABLE ProductCategories (
	Id INTEGER PRIMARY KEY AUTOINCREMENT,
	Title VARCHAR(25) NOT NULL
);

ALTER TABLE Products ADD COLUMN CategoryId INTEGER NOT NULL
	REFERENCES ProductCategories (Id) ON UPDATE RESTRICT ON DELETE RESTRICT;

INSERT INTO ProductCategories (Title) VALUES ('Category #1');
INSERT INTO ProductCategories (Title) VALUES ('Category #2');
INSERT INTO ProductCategories (Title) VALUES ('Category #3');

INSERT INTO Products (Title, Description, LongDescription, Price, CategoryId)
VALUES ('Product #1', 'This is a Product', 'This is a longer description of Product #1', 123.45, 1);

INSERT INTO Products (Title, Description, LongDescription, Price, CategoryId)
VALUES ('Product #2', 'This is a Product', 'This is a longer description of Product #2', 234.56, 1);

INSERT INTO Products (Title, Description, LongDescription, Price, CategoryId)
VALUES ('Product #3', 'This is a Product', 'This is a longer description of Product #3', 345.67, 2);

INSERT INTO Products (Title, Description, LongDescription, Price, CategoryId)
VALUES ('Wrong record', 'Wrong record', 'Wrong record', 0, 1);

UPDATE Products
SET Price = Price * 1.1
WHERE Id = 1;

DELETE FROM Products
WHERE Price = 0;

SELECT Title, Price
FROM Products
WHERE Price > 200;

SELECT *
FROM Products pr
INNER JOIN ProductCategories pc ON pr.CategoryId = pc.Id;

CREATE TABLE Customers (
	Id INTEGER PRIMARY KEY AUTOINCREMENT,
	Firstname VARCHAR(50) NOT NULL,
	Lastname VARCHAR(100) NOT NULL,
	Telephone VARCHAR(15) NOT NULL,
	`E-mail` VARCHAR(100) NOT NULL,
	DateOfBirth DATE NOT NULL
);

CREATE TABLE CustomerCredentials (
	CustomerId INTEGER PRIMARY KEY REFERENCES Customers (Id) ON UPDATE CASCADE ON DELETE CASCADE,
	Username VARCHAR(20) NOT NULL,
	PasswordHash VARCHAR(128) NOT NULL
);

CREATE TABLE Addresses (
	Id INTEGER PRIMARY KEY AUTOINCREMENT,
	Street VARCHAR(100) NOT NULL,
	Area VARCHAR(50) NOT NULL,
	Country VARCHAR(50) NOT NULL,
	CustomerId INTEGER NOT NULL REFERENCES Customer (Id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Orders (
	Id INTEGER PRIMARY KEY AUTOINCREMENT,
	Timestamp DATETIME DEFAULT (datetime('now','localtime')),
    Total DECIMAL(6,2) NOT NULL,
	CustomerId INTEGER NOT NULL REFERENCES Customer (Id) ON UPDATE CASCADE ON DELETE RESTRICT
);

SELECT *
FROM Orders
WHERE Total BETWEEN 1000 AND 2000;

CREATE TABLE OrderItems (
	OrderId INTEGER NOT NULL REFERENCES Orders (Id) ON UPDATE CASCADE ON DELETE CASCADE,
	ProductId INTEGER NOT NULL REFERENCES Products (Id) ON UPDATE CASCADE ON DELETE RESTRICT,
	PRIMARY KEY (OrderId, ProductId)
)

-- COMMIT TRANSACTION;
