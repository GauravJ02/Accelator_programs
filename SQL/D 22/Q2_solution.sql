/*Problem-2: Customer Order History Optimization (Composite Index)
Problem Statement:
Customers frequently check all their Delivered orders after logging into the
application. The dashboard filters records using Customer ID and Order Status.
As the number of orders has increased, dashboard loading has become slower.

Your Tasks
-------------
Display the execution plan before optimization.
Create a suitable Composite B-Tree Index.
Display the execution plan after optimization.
Execute the optimized query.


sample output;
--------------
+----+-------------+--------+------+--------------------------------------------+------------------------+---------+-------------+------+-------------+
| id | select_type | table  | type | possible_keys                              | key                    | key_len | ref         | rows | Extra       |
+----+-------------+--------+------+--------------------------------------------+------------------------+---------+-------------+------+-------------+
|  1 | SIMPLE      | Orders | ref  | idx_orders_cust_status,idx_customer_status | idx_orders_cust_status | 28      | const,const |    3 | Using where |
+----+-------------+--------+------+--------------------------------------------+------------------------+---------+-------------+------+-------------+
1 row in set (0.00 sec)


+----------+-------------+---------+----------+---------------------+-----------+--------------+
| order_id | customer_id | food_id | quantity | order_date          | status    | total_amount |
+----------+-------------+---------+----------+---------------------+-----------+--------------+
|        1 |           1 |       2 |        2 | 2026-07-10 12:30:00 | Delivered |       600.00 |
|        6 |           1 |       1 |        1 | 2026-07-13 14:00:00 | Delivered |       250.00 |
|       11 |           1 |       4 |       10 | 2026-07-16 18:00:00 | Delivered |       300.00 |
+----------+-------------+---------+----------+---------------------+-----------+--------------+
*/

EXPLAIN SELECT * FROM Orders WHERE customer_id = 1 AND status = 'Delivered';

CREATE INDEX idx_orders_cust_status ON Orders(customer_id, status);

EXPLAIN SELECT * FROM Orders WHERE customer_id = 1 AND status = 'Delivered';

SELECT * FROM Orders WHERE customer_id = 1 AND status = 'Delivered';
