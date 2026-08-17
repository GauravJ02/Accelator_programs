/*
Problem Description:
The operations desk wants to identify active premium menu categories that have successfully processed transactions. 
Write an SQL query that lists all unique food categories from the FoodItems table where the individual item price is greater than 150.
Use an INTERSECT operator to match these against categories that have at least one recorded entry in the Orders table.

case=1
output=
category
Main Course



*/
use fs;

SELECT 
    DISTINCT(category)
FROM FoodItems 
WHERE price > 150

INTERSECT

SELECT
    fi.category
FROM FoodItems fi
JOIN Orders o
    ON fi.food_id = o.food_id;