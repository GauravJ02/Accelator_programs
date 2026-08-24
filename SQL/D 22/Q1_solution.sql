/*
Problem 1: Customer Login Performance Optimization (B-Tree Index)
Problem Statement:
An online food delivery company has over 20 million registered customers.
During login, the application validates customers using their registered email address.
Recently, customer authentication has become noticeably slower during peak hours.
The database administrator wants to improve the query performance without modifying
the application logic.

your Task:
-------------
Create a suitable B-Tree Index.
Display the execution plan before optimization.
Display the execution plan after optimization.
Execute the optimized query.




*/

EXPLAIN SELECT * FROM Customers WHERE email = 'john.doe@example.com';

CREATE UNIQUE INDEX idx_customers_email ON Customers(email);

EXPLAIN SELECT * FROM Customers WHERE email = 'john.doe@example.com';

SELECT * FROM Customers WHERE email = 'john.doe@example.com';
