
/*
Problem Description:
The point-of-sale terminal supervisor wants to analyze processing batches to check for high-ticket individual item sales transactions.
Write an SQL query to list the order date, the count of unique orders placed on that date, and the maximum total amount recorded on a single order. 
Filter the groups to show only dates where the maximum individual order amount exceeds 300.


case=1
output=
explicit_date	total_orders	max_order_amount
2026-06-17	20	600.00


*/
use fs;

SELECT DATE(order_date) explicit_date, COUNT(DISTINCT order_id) total_orders, MAX(total_amount) max_order_amount
FROM Orders
GROUP BY DATE(order_date)
HAVING MAX(total_amount) > 300;