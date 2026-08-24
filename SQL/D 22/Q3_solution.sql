/*Problem-3: Restaurant Menu Search Optimization
Problem Statement:
The restaurant homepage displays all Main Course food items. Initially,
 the application performed a sequential scan because no index existed.
 As the menu size increased, page loading became slower. The administrator
 wants to compare sequential scanning with index scanning.


Student Tasks
----------------
Display the execution plan before optimization.
Create a suitable B-Tree Index.
Display the execution plan after optimization.
Execute the optimized query.
Compare Sequential Scan and Index Scan.

sample output:
------------
+----+-------------+-----------+------+---------------+--------------+---------+-------+------+-------------+
| id | select_type | table     | type | possible_keys | key          | key_len | ref   | rows | Extra       |
+----+-------------+-----------+------+---------------+--------------+---------+-------+------+-------------+
|  1 | SIMPLE      | FoodItems | ref  | idx_category  | idx_category | 52      | const |    2 | Using where |
+----+-------------+-----------+------+---------------+--------------+---------+-------+------+-------------+
1 row in set (0.00 sec)


+---------+----------------------+--------+-------------+--------------+
| food_id | name                 | price  | category    | availability |
+---------+----------------------+--------+-------------+--------------+
|       1 | Paneer Butter Masala | 250.00 | Main Course |            1 |
|       2 | Chicken Biryani      | 300.00 | Main Course |            1 |
+---------+----------------------+--------+-------------+--------------+
2 rows in set (0.00 sec)
*/
EXPLAIN SELECT * FROM FoodItems WHERE category = 'Main Course';

CREATE INDEX idx_category ON FoodItems(category);

EXPLAIN SELECT * FROM FoodItems WHERE category = 'Main Course';

SELECT * FROM FoodItems WHERE category = 'Main Course';

EXPLAIN SELECT * FROM FoodItems IGNORE INDEX (idx_category) WHERE category = 'Main Course';

EXPLAIN SELECT * FROM FoodItems FORCE INDEX (idx_category) WHERE category = 'Main Course';
