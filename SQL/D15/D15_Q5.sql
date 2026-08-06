/*
Problem Description:
The food truck operations desk wants to check the historical sales velocities specifically for quick-service categories. 
Write an SQL query to discover the order ID, the food item name, its category, and the quantity ordered.
Limit the rows to items classified under the 'Snacks' or 'Beverages' categories, and ensure only orders with an explicit quantity of 2 or more are returned. 
Sort the list by quantity in descending order.

case=1
output=
order_id	food_item_name	category	quantity
15	Samosa	Snacks	5
6	Samosa	Snacks	4
20	Mango Lassi	Beverages	3
13	Mango Lassi	Beverages	2



*/
use fs;

SELECT o.order_id, fi.name food_item_name, fi.category, o.quantity
FROM Orders o JOIN FoodItems fi
    ON o.food_id = fi.food_id
WHERE fi.category IN ("Snacks","Beverages") AND o.quantity >= 2
ORDER BY quantity DESC;
