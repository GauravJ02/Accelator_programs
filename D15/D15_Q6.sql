/*
Problem Description:
The reward and recognition committee is auditing the salary distribution across standard organizational tiers. 
Write an SQL query to find the salary grade numbers from the salgrade table along with the count of employees whose salaries fall into those respective grade brackets.
Only show grades that have more than 2 employees assigned to them, and sort the grades in ascending order.

case=1
output=
salary_grade	employee_count
1	8
2	10
3	7
4	6



*/
use fs;

SELECT sg.grade salary_grade, COUNT(e.empno) employee_count
FROM salgrade sg JOIN emp e
    ON e.sal BETWEEN sg.losal AND sg.hisal
GROUP BY sg.grade
HAVING COUNT(e.empno) > 2
ORDER BY salary_grade;