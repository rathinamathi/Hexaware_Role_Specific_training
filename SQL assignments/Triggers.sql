CREATE TABLE sales.order_status_audit (
    audit_id INT IDENTITY(1,1) PRIMARY KEY,
    order_id INT,
    old_status TINYINT,
    new_status TINYINT,
    change_date DATETIME DEFAULT GETDATE()
);

CREATE TRIGGER trg_order_status_update
ON sales.orders
AFTER UPDATE
AS
BEGIN
    INSERT INTO sales.order_status_audit(order_id, old_status, new_status)
    SELECT d.order_id, d.order_status, i.order_status
    FROM deleted d
    JOIN inserted i ON d.order_id = i.order_id
    WHERE d.order_status <> i.order_status;
END;

SELECT order_id, order_status
FROM sales.orders
WHERE order_id = 1;

UPDATE sales.orders
SET order_status = 2
WHERE order_id = 1;

SELECT *
FROM sales.order_status_audit
WHERE order_id = 1