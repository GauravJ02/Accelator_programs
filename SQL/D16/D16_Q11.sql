/*

Problem Description:
The business intelligence developer wants to identify high-value breakfast consumers to target with a new morning loyalty campaign.
Write a read-only SQL query to retrieve the customer's full name, email address, and their total lifetime spending across all menu categories.
Filter the output to return only those customers whose cumulative spending specifically on items in the 'Breakfast' category is 
strictly greater than the average breakfast expenditure calculated across all customers who have ordered breakfast.

case=1
output=
customer_name	email	total_lifetime_spending
Priya Singh	priya.singh@yahoo.com	680.00
Arjun Gupta	arjun.gupta@gmail.com	920.00



*/
use fs;

SELECT
    CONCAT_WS(" ", c.first_name, c.last_name) AS customer_name,
    c.email,
    SUM(o.total_amount) AS total_lifetime_spending
FROM Orders o
JOIN Customers c
    ON c.customer_id = o.customer_id
WHERE o.customer_id IN (
    SELECT bt.customer_id
    FROM (
        SELECT customer_id, SUM(total_amount) AS bft
        FROM Orders o2
        JOIN FoodItems fi ON fi.food_id = o2.food_id
        WHERE fi.category = 'Breakfast'
        GROUP BY o2.customer_id
    ) bt
    WHERE bt.bft > (
        SELECT AVG(bt2.bft)
        FROM (
            SELECT customer_id, SUM(total_amount) AS bft
            FROM Orders o2
            JOIN FoodItems fi ON fi.food_id = o2.food_id
            WHERE fi.category = 'Breakfast'
            GROUP BY o2.customer_id
        ) bt2
    )
)
GROUP BY c.email, c.first_name, c.last_name;