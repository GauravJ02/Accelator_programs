/*
Topic: Date Sequence Generation

Statement: Generate a sequence of daily dates from 2026-07-10 to 2026-07-17 to find dates where NO food orders were placed.

case=1
output=
order_date
2026-07-10
2026-07-11
2026-07-12
2026-07-13
2026-07-14
2026-07-15
2026-07-16
2026-07-17



*/
use fs;

WITH RECURSIVE date_sequence AS (

    -- Start date
    SELECT CAST('2026-07-10' AS DATE) AS order_date

    UNION ALL

    -- Generate next date
    SELECT DATE_ADD(order_date, INTERVAL 1 DAY)
    FROM date_sequence
    WHERE order_date < '2026-07-17'
)

SELECT
    d.order_date
FROM date_sequence d
LEFT JOIN Orders o
    ON d.order_date = DATE(o.order_date)
WHERE o.order_id IS NULL;