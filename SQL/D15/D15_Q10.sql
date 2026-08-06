
/*
Problem Description:
The financial controllers need to discover which active managers are supervising teams that consume large portions of the budget. 
Write an SQL query to pull the manager's employee number, the manager's name, and the sum total of all salaries earned by their immediate direct reports. 
Only return rows where the cumulative salary pool of subordinates is greater than 4000. Sort from highest pool to lowest.

case=1
output=
manager_id	manager_name	total_subordinate_payroll
7839	KEVIN	8275.00
7698	BLAKE	6550.00
7566	JONES	6000.00



*/
use fs;

SELECT m.empno manager_id, m.ename manager_name, SUM(e.sal) total_subordinate_payroll
FROM emp m JOIN emp e
    ON e.mgr = m.empno
GROUP BY m.empno, m.ename
HAVING SUM(e.sal) > 4000
ORDER BY total_subordinate_payroll DESC;