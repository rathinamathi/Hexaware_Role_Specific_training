SELECT 
s.store_name,
SUM(oi.quantity * oi.list_price) AS total_sales
FROM sales.stores s
JOIN sales.orders o ON s.store_id = o.store_id
JOIN sales.order_items oi ON o.order_id = oi.order_id
GROUP BY s.store_name
HAVING SUM(oi.quantity * oi.list_price) > 50000;


SELECT TOP 5 
p.product_name,
SUM(oi.quantity) AS total_quantity_sold
FROM sales.order_items oi
JOIN production.products p ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity_sold DESC;

SELECT 
FORMAT(o.order_date, 'yyyy-MM') AS month,
SUM(oi.quantity * oi.list_price) AS monthly_sales
FROM sales.orders o
JOIN sales.order_items oi ON o.order_id = oi.order_id
WHERE YEAR(o.order_date) = 2016
GROUP BY FORMAT(o.order_date, 'yyyy-MM')
ORDER BY month;

SELECT 
s.store_name,
SUM(oi.quantity * oi.list_price) AS total_revenue
FROM sales.stores s
JOIN sales.orders o ON s.store_id = o.store_id
JOIN sales.order_items oi ON o.order_id = oi.order_id
GROUP BY s.store_name
HAVING SUM(oi.quantity * oi.list_price) > 100000;

