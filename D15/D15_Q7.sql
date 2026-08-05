/*
Problem Description:
The corporate systems team needs a clean audit of team rosters reporting to specific mid-level managers. 
Write an SQL query to retrieve the employee name, their hire date, their salary, and their direct manager's name. 
Filter the records to include only employees who report to managers with the employee numbers 7698 or 7566,
and whose salary is greater than 1000. Sort the final output alphabetically by employee name.

case=1
output=
employee_name	hiredate	salary	manager_name
ALLEN	1998-08-15	1600.00	BLAKE
ALLEN	1996-03-26	1250.00	BLAKE
FORD	1997-12-05	3000.00	JONES
KEVIN	1995-06-04	1500.00	BLAKE
MARTIN	1998-12-05	1250.00	BLAKE
SCOTT	1996-03-05	3000.00	JONES



*/
use fs;

SELECT e.ename employee_name, e.hiredate, e.sal salary, m.ename manager_name
FROM emp e JOIN emp m
    ON e.mgr = m.empno
WHERE m.empno IN (7698,7566) AND e.sal > 1000
ORDER BY employee_name;