/*
Problem Description:
The operational marketing team wants to find the IDs of customers who have ordered 'Chicken Biryani' AND have ordered 'Mango Lassi', 
but have completely excluded 'Samosa' from their ordering lifetime history. Structure a combination of INTERSECT and EXCEPT clauses 
driven by internal target-matching subqueries to extract this precise segmentation.



case=1
output=
customer_id
4



*/
use fs;

SELECT 
    o.customer_id
FROM Orders o
JOIN FoodItems fi
    ON o.food_id = fi.food_id
WHERE fi.name = "Chicken Biryani"

INTERSECT

SELECT 
    o.customer_id
FROM Orders o
JOIN FoodItems fi
    ON o.food_id = fi.food_id
WHERE fi.name = "Mango Lassi"

EXCEPT

SELECT 
    o.customer_id
FROM Orders o
JOIN FoodItems fi
    ON o.food_id = fi.food_id
WHERE fi.name = "Samosa";