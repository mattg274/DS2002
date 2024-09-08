World Database
1) SELECT Name FROM country WHERE continent = "South America"
2) SELECT Population FROM country WHERE name = "Germany" 
3)  SELECT * from city where CountryCode = "JPN"
4) SELECT Name, Population FROM country WHERE Continent = 'Africa' ORDER BY Population DESC LIMIT 3
5) SELECT Name, LifeExpectancy FROM country WHERE Population BETWEEN 1000000 AND 5000000
6) SELECT Name FROM country JOIN countrylanguage ON country.code = countrylanguage.CountryCode WHERE countrylanguage.Language = "French" AND countrylanguage.IsOfficial = "T" 

Chinook Database
7) SELECT * FROM `Album` WHERE ArtistId = "1"
8) SELECT FirstName, LastName, Email FROM Customer WHERE Country = "Brazil" 
9)  SELECT * FROM Playlist;
10) SELECT * FROM Track WHERE GenreId = 1 
11) SELECT FirstName, LastName FROM Employee WHERE ReportsTo = (SELECT EmployeeId FROM Employee WHERE FirstName = ‘Nancy’ AND LastName = ‘Edwards’) 
12)   SELECT CustomerId,
    SUM(Total) AS TotalSales
FROM
    Invoice
GROUP BY
    CustomerId;


Part 2
1) 
CREATE TABLE Products (
	 ProductID INT AUTO_INCREMENT PRIMARY KEY, 
	 ProductName VARCHAR(255) NOT NULL, 
	 Price DECIMAL(10, 2) NOT NULL );

CREATE TABLE Customers ( 
	CustomerID INT AUTO_INCREMENT PRIMARY KEY, 
	FirstName VARCHAR(100), 
	LastName VARCHAR(100) );

CREATE TABLE Orders (  
	CustomerID INT, ProductID INT, 
	FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID), 
	FOREIGN KEY (ProductID) REFERENCES Products(ProductID) );

2) Insert Data

	INSERT INTO Products (ProductName, Price) VALUES 
		('Lacrosse Stick', 99.99), 		
		('Lacrosse Helmet', 149.99), 	
		('Lacrosse Gloves', 59.99), 
		('Lacrosse Pads', 89.99), 
		('Lacrosse Ball Pack', 19.99);

	INSERT INTO Customers (FirstName, LastName) VALUES 
	(‘Mark’, ‘Andrews), 
	(‘Romeo’, ‘Doubs), 
	(‘Christian’, ‘Kirk’), 
	(‘Josh’, ‘Palmer’), 
	(‘Terry’, ‘Mclaurin’);

	INSERT INTO Orders (CustomerID, ProductID) VALUES 
		(1, 1), 
		(2, 2),
		(3,3)
		(4,4)
		(5,5);

3)  Queries on new database
	List of all customers
		Select * FROM Customers

	List of Products and their prices
		SELECT ProductName, Price FROM Products

	Amount of times product 3 was ordered
		SELECT COUNT(*) AS TotalOrders FROM Orders WHERE ProductID = 3

	


