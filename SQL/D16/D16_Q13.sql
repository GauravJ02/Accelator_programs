/*
Problem Description:
The strategic analysis team requires a list of department numbers where the average employee salary is strictly greater than the company-wide average salary.
Additionally, these departments must also employ at least one worker who ranks among the highest-paid individuals in the company (specifically,
those earning a salary greater than or equal to the second-highest salary found in the entire organization). Write an SQL query using nested table 
derivatives, multi-level metrics, and an INTERSECT operator block to join these matching criteria groups cleanly without modifying any structural data.

case=1
output=
deptno
40




*/
use fs;

SELECT 
    d.deptno
FROM dept d
JOIN emp e
    ON d.deptno = e.deptno
GROUP BY d.deptno
HAVING AVG(e.sal) > (SELECT AVG(sal) FROM emp)

INTERSECT

SELECT 
    d.deptno
FROM dept d
JOIN emp e
    ON d.deptno = e.deptno
WHERE e.sal >= (SELECT sal FROM emp WHERE sal < (SELECT MAX(sal) FROM emp) ORDER BY sal DESC LIMIT 1);