/*
An enterprise data analyst needs to audit high-performing customer accounts to identify regional market leaders.
Write a read-only SQL query to find the customer ID, their full name (first name and last name combined), their city address, 
and their total lifetime expenditure across all orders.

Filter the results using a complex correlated subquery inside the HAVING clause so that you only return customers whose 
cumulative lifetime spending is strictly greater than the historical average of individual transaction amounts placed by all customers living in that exact same city.

case=1
output=
customer_id	customer_name	city_address	total_customer_lifetime_spend
4	Neha Patel	Ahmedabad, India	1020.00
5	Arjun Gupta	Hyderabad, India	920.00
3	Rahul Verma	Bengaluru, India	860.00
1	Amit Sharma	Delhi, India	730.00
2	Priya Singh	Mumbai, India	680.00

*/
use fs;

SELECT 
    c.customer_id,
    CONCAT_WS(' ',c.first_name,c.last_name) AS customer_name,
    c.address AS city_address,
    SUM(o.total_amount) AS total_customer_lifetime_spend
FROM Customers c
JOIN Orders o
    ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_id,
    c.first_name,
    c.last_name,
    c.address
HAVING SUM(o.total_amount) > (SELECT AVG(o2.total_amount) FROM Orders o2 JOIN Customers c2 ON o2.customer_id = c2.customer_id WHERE c2.address = c.address)
ORDER BY total_customer_lifetime_spend DESC;