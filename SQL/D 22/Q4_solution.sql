/*Problem-4: Employee Department Search Optimization
Problem Statement
--------------------
The Human Resources department frequently retrieves all employees working
in Department 20 while preparing payroll reports. The employee table has
grown significantly, causing slower query execution. The administrator wants
to optimize the search.

Your Tasks:
--------------
Display the execution plan before optimization.
Create a suitable Hash Index.
Display the execution plan after optimization.
Execute the optimized query.

Expected output:
------------------
+----+-------------+-------+------+---------------+--------------+---------+-------+------+-------------+
| id | select_type | table | type | possible_keys | key          | key_len | ref   | rows | Extra       |
+----+-------------+-------+------+---------------+--------------+---------+-------+------+-------------+
|  1 | SIMPLE      | emp   | ref  | idx_emp_dept  | idx_emp_dept | 5       | const |    5 | Using where |
+----+-------------+-------+------+---------------+--------------+---------+-------+------+-------------+
1 row in set (0.00 sec)


+-------+-------+---------+------+------------+---------+------+--------+
| empno | ename | job     | mgr  | hiredate   | sal     | comm | deptno |
+-------+-------+---------+------+------------+---------+------+--------+
|  7369 | SMITH | CLERK   | 7902 | 2023-12-17 | 1007.77 | 0.00 |     20 |
|  7566 | JONES | MANAGER | 7839 | 2022-04-02 | 3747.64 | NULL |     20 |
|  7788 | SCOTT | ANALYST | 7566 | 2024-04-19 | 3779.14 | NULL |     20 |
|  7876 | ADAMS | CLERK   | 7788 | 2024-05-23 | 1385.68 | NULL |     20 |
|  7902 | FORD  | ANALYST | 7566 | 2022-12-03 | 3779.14 | NULL |     20 |
+-------+-------+---------+------+------------+---------+------+--------+
5 rows in set (0.00 sec)
*/
EXPLAIN SELECT * FROM emp WHERE deptno = 20;

CREATE INDEX idx_emp_dept ON emp(deptno) USING HASH;

EXPLAIN SELECT * FROM emp WHERE deptno = 20;

SELECT * FROM emp WHERE deptno = 20;
