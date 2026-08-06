/*
Problem Description:
The shipping coordinators want to find unique transaction entries where a customer bought an unusually high volume of an individual item in a single order line.
Write an SQL query to find the order ID, customer ID, and the maximum quantity ordered in a single transaction. 
Filter the rows down to only showcase orders where the individual quantity is 3 or more and the status is listed as 'Delivered' or 'Preparing'.

case=1
output=
order_id	customer_id	maximum_quantity
15	5	5
6	2	4
12	4	4
16	5	4
2	1	3
14	5	3
20	3	3

*/
use fs;

SELECT o.order_id, o.customer_id, o.quantity as maximum_quantity
FROM Orders o
WHERE (o.status = "Delivered" OR o.status = "Preparing") AND o.quantity >= 3
ORDER BY maximum_quantity DESC;