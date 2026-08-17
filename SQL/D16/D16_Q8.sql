/*
Problem Description:
The payroll department wants to pinpoint specific regional departments where the cumulative operational costs (sum of all employee salaries) 
are entirely driven by staff members hired in the 1990s decade. Write an SQL query using nested subquery groups that evaluates 
the total salary of employees hired between 1990 and 1999 and matches it against the absolute department total payroll.

case=1
output=
deptno	dname
30	Sales
40	Operations


*/
use fs;

SELECT 
    d.deptno,
    d.dname
FROM dept d
JOIN emp e
    ON d.deptno = e.deptno
GROUP BY d.deptno
HAVING SUM(e.sal) = (SELECT SUM(e.sal) FROM emp e WHERE YEAR(e.hiredate) BETWEEN 1990 AND 1999 AND e.deptno = d.deptno);