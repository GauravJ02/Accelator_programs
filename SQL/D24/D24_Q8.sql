/*

Topic: Top-Down Hierarchy with Depth & Path Generation

Statement: Generate a full hierarchy starting from top management (mgr IS NULL), assigning organizational levels (1, 2, 3...) and displaying the management path string (e.g., KEVIN -> JONES -> FORD).

case=1
output=
empno	ename	lvl	path
7839	KEVIN	1	KEVIN
7566	JONES	2	KEVIN -> JONES
7698	BLAKE	2	KEVIN -> BLAKE
7782	CLARK	2	KEVIN -> CLARK
7499	ALLEN	3	KEVIN -> BLAKE -> ALLEN
7521	ALLEN	3	KEVIN -> BLAKE -> ALLEN
7654	MARTIN	3	KEVIN -> BLAKE -> MARTIN
7788	SCOTT	3	KEVIN -> JONES -> SCOTT
7844	KEVIN	3	KEVIN -> BLAKE -> KEVIN
7900	JAMES	3	KEVIN -> BLAKE -> JAMES
7902	FORD	3	KEVIN -> JONES -> FORD
7934	FORD	3	KEVIN -> CLARK -> FORD
7369	SMITH	4	KEVIN -> JONES -> FORD -> SMITH
7876	KEVIN	4	KEVIN -> JONES -> SCOTT -> KEVIN



*/
use fs;

WITH RECURSIVE employee_hierarchy AS (

    -- Anchor: top-level management
    SELECT
        empno,
        ename,
        1 AS lvl,
        CAST(ename AS CHAR(1000)) AS path
    FROM emp
    WHERE mgr IS NULL

    UNION ALL

    -- Recursive: find employees reporting to current employee
    SELECT
        e.empno,
        e.ename,
        h.lvl + 1 AS lvl,
        CONCAT(h.path, ' -> ', e.ename) AS path
    FROM emp e
    JOIN employee_hierarchy h
        ON e.mgr = h.empno
)

SELECT
    empno,
    ename,
    lvl,
    path
FROM employee_hierarchy;