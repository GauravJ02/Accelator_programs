/*

Problem Description:
The HR director wants to assess the management overhead by analyzing salary distributions mapped to individual supervisors. 
Write an SQL query to fetch the manager's name and the average salary of the employees who report directly to them. 
Group the data by the manager's identity, and only include managers where the average salary of their subordinates exceeds 1500.
Sort the final output by average salary in descending order.

case=1
output=
manager_name	average_subordinate_salary
JONES	3000.000000
KEVIN	2758.333333

*/
use fs;

SELECT m.ename manager_name, AVG(e.sal) average_subordinate_salary
FROM emp m JOIN emp e
    ON e.mgr = m.empno
GROUP BY m.empno
HAVING AVG(e.sal) > 1500
ORDER BY average_subordinate_salary DESC;