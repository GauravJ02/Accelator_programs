/*
The internal auditing team is standardizing escalation pathways across the entire 
workforce. For every employee listed in the company, they need to identify the 
ultimate executive supervisor at the very top of their reporting chain 
(where no higher manager exists). This mapping will establish clear chains 
of command from frontline staff directly up to executive management.

case=1
output=
original_emp	ultimate_boss
7839	KEVIN
7566	KEVIN
7698	KEVIN
7782	KEVIN
7499	KEVIN
7521	KEVIN
7654	KEVIN
7788	KEVIN
7844	KEVIN
7900	KEVIN
7902	KEVIN
7934	KEVIN
7369	KEVIN
7876	KEVIN



*/
use fs;

WITH RECURSIVE boss_chain AS (
    SELECT empno AS original_emp, empno AS current_emp, ename AS current_name, mgr
    FROM emp

    UNION ALL

    SELECT bc.original_emp, e.empno, e.ename, e.mgr
    FROM emp e
    JOIN boss_chain bc ON e.empno = bc.mgr
)
SELECT original_emp, current_name AS ultimate_boss
FROM boss_chain
WHERE mgr IS NULL;