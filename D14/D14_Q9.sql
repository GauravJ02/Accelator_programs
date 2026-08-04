/*

Problem Description:
The operational audit team wants to review veterans working in key corporate locations to schedule long-service awards. 
Write an SQL query to retrieve the employee name, their hire date, their job description, and their department location. 
Filter the records to only display employees who were hired before January 1, 1997, and who are located in 'Dallas' or 'New York'. 
Sort the output so that the longest-serving employee appears first.



case=1
output=
employee_name	hiredate	job	location
CLARK	1993-05-14	MANAGER	New York
SMITH	1993-06-13	CLERK	Dallas
JONES	1995-10-31	MANAGER	Dallas
SCOTT	1996-03-05	ANALYST	Dallas

*/
use fs;

SELECT e.ename employee_name, e.hiredate hiredate, e.job job, d.location location
FROM emp e JOIN dept d ON e.deptno = d.deptno
WHERE e.hiredate < "1997-01-01" AND d.location IN ("Dallas", "New York")
ORDER BY hiredate;