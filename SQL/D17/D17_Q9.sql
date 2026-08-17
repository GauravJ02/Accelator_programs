/*
The internal audit department needs a unified exception report detailing extreme pay scenarios across corporate levels. 
Write a read-only SQL query that extracts the employee name, their supervisor's name, and their salary for employees 
who earn more money than their direct supervisor. Use a UNION ALL block to append another dataset matching high-earner outliers: 
employees whose base salary is strictly greater than the calculated average salary of all active managers combined.

case=1
output=
employee_name	manager_name	employee_salary
SCOTT	JONES	3000.00
FORD	JONES	3000.00
KEVIN	N/A - System Outlier	5000.00



*/
use fs;

SELECT 
    e.ename AS employee_name,
    m.ename AS manager_name,
    e.sal AS employee_salary
FROM emp e
JOIN emp m
    ON e.mgr = m.empno
WHERE e.sal > m.sal

UNION ALL 

SELECT 
    e.ename AS employee_name,
    'N/A - System Outlier' AS manager_name,
    e.sal AS employee_salary
FROM emp e
WHERE e.sal > (SELECT AVG(m2.sal) FROM emp e2 JOIN emp m2 ON m2.empno = e2.mgr);
