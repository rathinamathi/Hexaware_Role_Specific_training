CREATE TABLE price_change_log(
log_id INT IDENTITY(1,1) PRIMARY KEY,
product_id INT,
old_price DECIMAL(10,2),
new_price DECIMAL(10,2),
change_date DATETIME DEFAULT GETDATE()
);

CREATE TRIGGER trg_priceChangeLog
ON production.products
AFTER UPDATE
AS 
BEGIN
INSERT INTO price_change_log (product_id,old_price,new_price)
SELECT i.product_id,d.list_price,i.list_price
FROM inserted i
JOIN deleted d ON i.product_id = d.product_id
WHERE i.list_price <> d.list_price;
END


SELECT product_id, product_name, list_price
FROM production.products
WHERE product_id = 1;

UPDATE production.products
SET list_price = 500.67  
WHERE product_id = 1;

SELECT * FROM price_change_log



select * from sales.orders

CREATE TRIGGER trg_prevent_product_delete
ON production.products
INSTEAD OF DELETE
AS
BEGIN
IF EXISTS (
SELECT 1
FROM deleted d
JOIN sales.order_items oi ON d.product_id = oi.product_id
JOIN sales.orders o ON oi.order_id = o.order_id
WHERE o.order_status = 1
    )
BEGIN
ROLLBACK TRANSACTION;
RETURN;
END
DELETE FROM production.products
WHERE product_id IN (SELECT product_id FROM deleted);
END;
