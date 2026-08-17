/*
Problem Description:
The analytics desk wants to compile a list of highly engaged customer contacts for a targeted outreach program. 
Write a read-only query that uses the UNION operator to find the unique customer IDs, first names, and emails of customers
who have either placed a single order exceeding a quantity of 3 or have successfully spent more than 300.00 in a single transaction.



case=1
output=
customer_id	first_name	email
2	Priya	priya.singh@yahoo.com
4	Neha	neha.patel@yahoo.com
5	Arjun	arjun.gupta@gmail.com



*/
use fs;

SELECT 
    c.customer_id,
    first_name,
    email
FROM Customers c
JOIN Orders o
    ON c.customer_id = o.customer_id
WHERE o.quantity > 3

UNION

SELECT 
    c.customer_id,
    first_name,
    email
FROM Customers c
JOIN Orders o
    ON c.customer_id = o.customer_id
WHERE o.total_amount > 300;