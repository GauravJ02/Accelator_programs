/*Problem-5: Food Name Lookup Optimization (Covering Index)
Problem Statement:
Customers frequently search for Chicken Biryani before placing orders.
The application displays only the food name and price. The administrator
wants to reduce table access by creating a suitable covering index.

Student Tasks
--------------
Display the execution plan before optimization.
Create a suitable Covering Index.
Display the execution plan after optimization.
Execute the optimized query.


Expected output:
------------------
+----+-------------+-----------+------+----------------+----------------+---------+-------+------+--------------------------+
| id | select_type | table     | type | possible_keys  | key            | key_len | ref   | rows | Extra                    |
+----+-------------+-----------+------+----------------+----------------+---------+-------+------+--------------------------+
|  1 | SIMPLE      | FoodItems | ref  | idx_food_cover | idx_food_cover | 102     | const |    1 | Using where; Using index |
+----+-------------+-----------+------+----------------+----------------+---------+-------+------+--------------------------+
1 row in set (0.00 sec)


+-----------------+--------+
| name            | price  |
+-----------------+--------+
| Chicken Biryani | 300.00 |
+-----------------+--------+
1 row in set (0.01 sec)
*/
EXPLAIN SELECT name, price FROM FoodItems WHERE name = 'Chicken Biryani';

CREATE INDEX idx_food_cover ON FoodItems(name, price);

EXPLAIN SELECT name, price FROM FoodItems WHERE name = 'Chicken Biryani';

SELECT name, price FROM FoodItems WHERE name = 'Chicken Biryani';
