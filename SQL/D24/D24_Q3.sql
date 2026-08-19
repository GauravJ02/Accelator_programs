/*
Problem 2 (Medium): Above-Average Departmental Salaries
Topic: CTE Chaining

Statement: The HR department wants to find employees whose salary is higher than their department’s average salary. Use two chained CTEs: one to calculate department averages and another to filter employees. Display empno, ename, sal, and deptno.

case=1
output=

empno	ename	sal	deptno
7566	JONES	2975.00	20
7698	BLAKE	2850.00	30
7782	CLARK	2450.00	10
7788	SCOTT	3000.00	20
7839	KEVIN	5000.00	40
7902	FORD	3000.00	20


*/
use fs;

USE fs;

WITH dept_avg AS (
    SELECT
        deptno,
        AVG(sal) AS avg_salary
    FROM emp
    GROUP BY deptno
),
above_avg AS (
    SELECT
        e.empno,
        e.ename,
        e.sal,
        e.deptno
    FROM emp e
    JOIN dept_avg d
        ON e.deptno = d.deptno
    WHERE e.sal > d.avg_salary
)
SELECT
    empno,
    ename,
    sal,
    deptno
FROM above_avg;