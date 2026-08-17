/*
Problem Description:
An enterprise HR metrics developer needs to flag anomalous salaries where individuals out-earn the localized aggregate averages. 
Write a read-only SQL query to extract the employee name, department name, location, and salary from the emp and dept tables. 
The query must use nested subqueries to filter and return only those employees whose salary is strictly greater than the average 
salary of the entire department that holds the maximum aggregate payroll budget across the company.  

case=1
output=
employee_name	department_name	location	salary
JONES	Research	Dallas	2975.00
BLAKE	Sales	Chicago	2850.00
CLARK	Accounting	New York	2450.00
SCOTT	Research	Dallas	3000.00
KEVIN	Operations	Boston	5000.00
FORD	Research	Dallas	3000.00



*/
use fs;

SELECT 
    e.ename AS employee_name,
    d.dname AS department_name,
    d.location,
    e.sal AS salary
FROM emp e
JOIN dept d
    ON e.deptno = d.deptno
WHERE e.sal > (SELECT AVG(e1.sal) FROM emp e1 JOIN dept d1 ON e1.deptno = d1.deptno WHERE d1.deptno = (SELECT dt.deptno FROM (SELECT SUM(sal) AS agg ,e.deptno FROM emp e JOIN dept d ON d.deptno = e.deptno GROUP BY d.deptno) dt ORDER BY dt.agg DESC LIMIT 1));