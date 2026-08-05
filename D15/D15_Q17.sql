/*
Problem Description:
The HR department wants to audit regional branches that currently house active analytical or technical staff. 
Write an SQL query to extract the department number, department name, and regional location from the dept table. 
Use a correlated subquery with an EXISTS operator to filter for departments that have at least one employee working as an 'ANALYST'.

case=1
output=
deptno	dname	location
20	Research	Dallas



*/
use fs;

SELECT 
    deptno,
    dname,
    location
FROM dept d
WHERE EXISTS (SELECT * FROM emp e WHERE e.job = "ANALYST" AND e.deptno = d.deptno);