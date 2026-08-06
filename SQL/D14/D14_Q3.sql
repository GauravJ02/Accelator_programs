/*
Problem Description:
The sales operations team wants to analyze high-performing sales representatives who are generating substantial revenue through commissions. 
Write an SQL query to retrieve the employee's name, their job title, their department's name, and their total compensation (calculated as salary plus commission).
Filter the results to include only employees whose job is 'SALESMAN', whose commission is strictly greater than 0, and 
who work in departments located in either 'Chicago' or 'Tempe'. 
Sort the output by the calculated total compensation in descending order.


case=1
output=
employee_name	job_title	department_name	total_compensation
ALLEN	SALESMAN	Sales	1750.00

*/

use fs;

SELECT e.ename as employee_name, e.job as job_title, d.dname as department_name, e.sal + e.comm as total_compensation
FROM emp as e JOIN dept as d ON e.deptno = d.deptno
WHERE e.comm > 0 AND d.location IN ("Chicago","Tempe")
GROUP BY e.empno
HAVING job_title = "SALESMAN"
ORDER BY e.sal + e.comm;