/*
Problem Description:
The HR department wants to audit departments that have a functional management footprint. 
Write a read-only SQL query to retrieve the department number and department name from the dept table.
Filter the output using an EXISTS correlated subquery to return only those departments that currently 
act as a workspace for at least one employee holding the job title of 'MANAGER'.

case=1
output=
deptno	dname
10	Accounting
20	Research
30	Sales


*/
use fs;

SELECT
    d.deptno,
    d.dname
FROM dept d 
WHERE EXISTS (SELECT e.deptno FROM emp e WHERE d.deptno = e.deptno AND e.job = 'MANAGER');