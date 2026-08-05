/*
Problem Description:
The organizational analysts want to check the distribution of specific clerical and administrative roles across standard corporate branches.
Write an SQL query to find the employee's name, their job, their department number, and the department name.
Filter the rows to include only those employees whose job role is exactly 'CLERK' and whose department is not located in 'New York'. 
Sort the results alphabetically by the employee's name.


case=1
output=
employee_name	job	deptno	department_name
JAMES	CLERK	20	Research
KEVIN	CLERK	20	Research
SMITH	CLERK	20	Research


*/
USE fs;

SELECT e.ename employee_name, e.job, e.deptno, d.dname department_name
FROM emp e JOIN dept d
    ON e.deptno = d.deptno
WHERE e.job = "CLERK" AND d.location <> "New York"
ORDER BY employee_name;