/*
Problem Description:
The executive committee needs an audit report containing the details of all employees who are either 
the absolute lowest earner in their respective department, or hold the maximum tenure (earliest hire date) 
across the whole company. Bring these two distinct granular groups together into one dataset matrix 
by joining them using a UNION ALL set operator.

case=1
output=
empno	ename	deptno	audit_tag
7369	SMITH	20	Lowest Department Earner
7521	ALLEN	30	Lowest Department Earner
7654	MARTIN	40	Lowest Department Earner
7934	FORD	10	Lowest Department Earner
7839	KEVIN	40	Company Senior Tenure



*/
use fs;

SELECT 
    e.empno,
    e.ename,
    e.deptno,
    "Lowest Department Earner" AS audit_tag
FROM emp e
WHERE e.sal = (SELECT MIN(e1.sal) FROM emp e1 WHERE e.deptno = e1.deptno)

UNION ALL

SELECT 
    e.empno,
    e.ename,
    e.deptno,
    "Company Senior Tenure" AS audit_tag
FROM emp e
WHERE e.hiredate = (SELECT MIN(e1.hiredate) FROM emp e1); 