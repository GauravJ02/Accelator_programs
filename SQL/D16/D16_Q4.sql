/*
Problem Description:
The HR system requires a comprehensive master list showing distinct employee tracks who are either working in top salary tiers (Grade 4 or 5) 
within a department located in 'Chicago', or are direct supervisors tracking subordinates who make less than 1500 base salary. 
Use structural subqueries combined with a UNION clause to bring these distinct operational groups together.

case=1
output=
empno	ename	classification_reason
7698	BLAKE	High Salary Tier in Chicago
7902	FORD	Manages Underpaid Subordinates
7698	BLAKE	Manages Underpaid Subordinates
7788	SCOTT	Manages Underpaid Subordinates
7782	CLARK	Manages Underpaid Subordinates



*/
use fs;

SELECT 
    e.empno,
    e.ename,
    "High Salary Tier in Chicago" AS classification_reason
FROM emp e
JOIN dept d
    ON e.deptno = d.deptno
JOIN salgrade sg 
    ON e.sal BETWEEN sg.losal AND sg.hisal
WHERE d.location = "Chicago" AND sg.grade IN (4,5)

UNION

SELECT 
    m.empno,
    m.ename,
    "Manages Underpaid Subordinates" AS classification_reason
FROM emp e
JOIN emp m
    ON e.mgr = m.empno
WHERE e.sal < 1500;