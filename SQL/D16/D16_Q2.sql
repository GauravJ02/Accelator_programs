/*
Problem Description:
The strategic analysts require a list of departments where the average employee salary is greater than the company-wide average salary, 
and which also employ at least one worker who ranks in the top earner brackets across the entire company. Write an SQL query using nested table derivatives,
multi-level scalar metrics, and an INTERSECT operator block to join these matching criteria groups cleanly.

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
HAVING AVG(e.sal) > (SELECT AVG(sal) FROM emp e) 

INTERSECT 

SELECT
    e.deptno
FROM emp e
JOIN salgrade sg 
    ON e.sal BETWEEN sg.losal AND sg.hisal
WHERE sg.grade = (SELECT MAX(grade) FROM salgrade);