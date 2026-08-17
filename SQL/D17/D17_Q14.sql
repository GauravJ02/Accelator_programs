/*
Problem Description:
The HR planning board requires a workspace distribution matrix to analyze operational units. Write a read-only SQL query to find the department number, 
department name, and the sum of salaries from the employee database. Filter the final rows using a multi-layered nested subquery 
inside the HAVING clause so that you only return organizational units whose total active employee headcount is strictly greater than 
the average employee headcount computed across all active departments in the enterprise.

case=1
output=
deptno	dname	total_department_payroll
20	Research	11825.00



*/
use fs;

SELECT
    d.deptno,
    d.dname,
    SUM(e.sal) AS total_department_payroll
FROM emp e
JOIN dept d
    ON e.deptno = d.deptno
GROUP BY 
    d.deptno,
    d.dname
HAVING COUNT(e.empno) > (SELECT AVG(dt.headcount) FROM (SELECT deptno, COUNT(empno) AS headcount FROM emp GROUP BY deptno) dt)