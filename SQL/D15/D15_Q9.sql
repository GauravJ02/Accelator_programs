/*
Problem Description:
The email marketing team is preparing a specific discount campaign targeting users on legacy email platforms.
Write an SQL query to find the customer's full name, email address, physical location, and the total quantity of items they ordered across all transactions.
Limit the base records to customers whose email ends with '@yahoo.com'.
Sort the output based on the total quantity in descending order.

case=1
output=
customer_name	email	address	total_quantity_ordered
Priya Singh	priya.singh@yahoo.com	Mumbai, India	9
Neha Patel	neha.patel@yahoo.com	Ahmedabad, India	9



*/
use fs;

SELECT CONCAT(c.first_name," ",c.last_name) customer_name, c.email, c.address, SUM(o.quantity) total_quantity_ordered
FROM Customers c JOIN Orders o
    ON c.customer_id = o.customer_id
WHERE c.email LIKE "%@yahoo.com"
GROUP BY CONCAT(c.first_name," ",c.last_name), c.email, c.address
ORDER BY total_quantity_ordered DESC;