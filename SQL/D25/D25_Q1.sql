/*
Problem Statement:

The HR department wants to assess the financial impact of the sales organization 
managed by BLAKE (Employee ID 7698). They need to calculate the total salary budget
allocated to BLAKE and every direct or indirect report under his command chain. 
To ensure accurate budgeting, the report must aggregate the total team headcount
and total salary payout across all levels of his department subtree.



case=1
output=
total_team_members	total_team_salary
6	9400.00



*/
use fs;

WITH RECURSIVE team AS(
    SELECT empno, ename, sal, mgr
    FROM emp 
    WHERE empno = 7698
    
    UNION ALL 
    
    SELECT e.empno, e.ename, e.sal, e.mgr
    FROM emp e
    JOIN team t
        ON e.mgr = t.empno
)
SELECT COUNT(empno) AS total_team_members, SUM(sal) AS total_team_salary FROM team;