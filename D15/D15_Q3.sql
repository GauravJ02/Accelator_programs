/*
Problem Description:
The sales strategy division wants to measure regional market penetration by identifying if there are registered customer locations that have zero transaction footprint. 
Write an SQL query to select each customer's address, full name, and the total number of orders they have placed.
Use an appropriate join to ensure that customers who have never placed an order are still listed with an order count of 0.

case=1
output=
address	customer_name	total_orders_placed
Delhi, India	Amit Sharma	4
Mumbai, India	Priya Singh	4
Bengaluru, India	Rahul Verma	4
Ahmedabad, India	Neha Patel	4
Hyderabad, India	Arjun Gupta	4


*/
use fs;

SELECT c.address, CONCAT(c.first_name," ",c.last_name) customer_name, COUNT(o.customer_id) total_orders_placed
FROM Customers c LEFT JOIN Orders o 
    ON o.customer_id = c.customer_id
GROUP BY c.address, customer_name;