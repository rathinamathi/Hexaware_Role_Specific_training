create database sample_db

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Price DECIMAL(10,2),
    InStock BIT
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
    Quantity INT,
    OrderDate DATE
);

INSERT INTO Products VALUES
(1, 'Laptop', 75000.00, 1),
(2, 'Mouse', 500.00, 1),
(3, 'Keyboard', 1500.00, 0);

INSERT INTO Orders VALUES
(101, 1, 2, '2025-07-20'),
(102, 2, 5, '2025-07-21');

SELECT * FROM Orders

CREATE VIEW vw_ordersOnly
AS 
SELECT OrderID, ProductID, Quantity, OrderDate 
FROM Orders;

SELECT * FROM vw_ordersOnly;

INSERT INTO vw_ordersOnly VALUES (103,2,3,'2025-07-22')

UPDATE vw_ordersOnly
SET Quantity = 10
WHERE OrderID = 103

DELETE FROM vw_ordersOnly WHERE OrderID=103

CREATE VIEW vw_ActiveOrders
AS
SELECT 
    o.OrderID, p.ProductName,o.Quantity,p.Price,
    (o.Quantity * p.Price) AS TotalAmount,
    o.OrderDate
FROM Orders o
JOIN Products p ON o.ProductID = p.ProductID
WHERE p.InStock = 1;

SELECT * FROM vw_ActiveOrders;

CREATE VIEW vw_SecureData
WITH ENCRYPTION
AS
SELECT * FROM Products;


sp_helptext 'vw_ActiveOrders'

sp_helptext 'SecureData'




