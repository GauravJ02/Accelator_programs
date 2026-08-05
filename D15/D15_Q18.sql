/*
Problem Description:
The financial control team wants to flag departments whose total payroll expenditure exceeds the average department-wise payroll across the company. 
Write an SQL query to find the department number and the sum of salaries for these high-expense departments. 
Group the records by department number and use a subquery inside the HAVING clause to benchmark against the overall average departmental total salary pool.

case=1
output=
deptno	total_payroll
20	11825.00



*/
use fs;

SELECT 
    d.deptno,
    SUM(e.sal) AS total_payroll
FROM dept d
JOIN emp e
    ON d.deptno = e.deptno
GROUP BY d.deptno
HAVING SUM(e.sal) > (SELECT AVG(total_payroll) FROM (SELECT deptno, SUM(sal) AS total_payroll FROM emp GROUP BY deptno) AS dept_payroll);