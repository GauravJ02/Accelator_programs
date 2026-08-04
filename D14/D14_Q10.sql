/*
Problem Description:
The business development team wants to reward loyal customers who frequently spend money on non-cancelled orders. 
Write an SQL query to find the customer ID, email address, and the total cumulative amount spent across all their orders. 
Exclude any orders that have a status of 'Cancelled' from the aggregation, and only include customers whose total spending exceeds 500. 
Order the final output from highest spending to lowest spending.

case=1
output=
customer_id	email	total_amount_spent
4	neha.patel@yahoo.com	1020.00
5	arjun.gupta@gmail.com	920.00
1	amit.sharma@gmail.com	730.00
2	priya.singh@yahoo.com	680.00
3	rahul.verma@gmail.com	610.00


*/
use fs;

SELECT c.customer_id, c.email, SUM(o.total_amount) total_amount_spent
FROM Customers c JOIN Orders o 
    ON c.customer_id = o.customer_id
WHERE o.status <> "Cancelled" 
GROUP BY c.customer_id, c.email
HAVING SUM(o.total_amount) > 500
ORDER BY total_amount_spent DESC;