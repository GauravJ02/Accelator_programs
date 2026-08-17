/*
Problem Description:
The HR systems division requires a comprehensive analytics list showing distinct employee tracks who meet high-profile administrative conditions. 
The report needs to display employees who are either working in top salary tiers (Grade 4 or 5) within a department located in 'Chicago', 
or are direct supervisors tracking subordinates who make less than 1500 base salary. Use structural analytical subqueries combined with
a UNION clause to compile these distinct operational groups together.

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
    'High Salary Tier in Chicago' AS classification_reason
FROM emp e
JOIN salgrade sg 
    ON e.sal BETWEEN sg.losal AND sg.hisal
JOIN dept d
    ON d.deptno = e.deptno
WHERE sg.grade IN (4,5) AND d.location = 'Chicago'

UNION

SELECT 
    e.empno,
    e.ename,
    'Manages Underpaid Subordinates' AS classification_reason
FROM emp e
JOIN emp f
    ON e.empno = f.mgr
WHERE f.sal < 1500;