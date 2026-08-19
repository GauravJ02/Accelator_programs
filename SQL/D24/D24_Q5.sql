/*
Topic: Chained CTEs across Non-Equi Joins

Statement: Categorize employees by salary grade, compute total salary spent per grade, and list grades accounting for more than ₹5,000 in salary payout. Display grade, employee_count, and total_grade_sal.

case=1
output=

grade	employee_count	total_grade_sal
1	8	9750.00
3	7	17375.00
2	10	21175.00
4	6	19275.00


*/
use fs;

WITH employee_grades AS (
    SELECT
        e.empno,
        e.sal,
        s.grade
    FROM emp e
    JOIN salgrade s
        ON e.sal BETWEEN s.losal AND s.hisal
),
grade_summary AS (
    SELECT
        grade,
        COUNT(*) AS employee_count,
        SUM(sal) AS total_grade_sal
    FROM employee_grades
    GROUP BY grade
)
SELECT
    grade,
    employee_count,
    total_grade_sal
FROM grade_summary
WHERE total_grade_sal > 5000;