/*
Problem Description:
The restaurant finance team wants to audit the total revenue generated from high-value food items.
Write an SQL query to find the food item name, its category, and the total revenue generated from it (calculated as the sum of the total amount across all orders).
Only include items belonging to the 'Main Course' or 'Breakfast' categories where the item has been ordered a total quantity of more than 2 times. 
Sort the results by total revenue in descending order.

case=1
output=
food_item_name	category	total_revenue
Chicken Biryani	Main Course	900.00
Masala Dosa	Breakfast	600.00
Veg Fried Rice	Main Course	390.00
Chole Bhature	Breakfast	300.00

*/


use fs;

SELECT 
    fi.name as food_item_name, 
    fi.category as category, 
    SUM(o.total_amount) as total_revenue
FROM 
    FoodItems fi 
    JOIN Orders o
    ON fi.food_id = o.food_id
WHERE fi.category IN ("Main Course","Breakfast")
GROUP BY fi.name,fi.category
HAVING SUM(o.quantity) > 2
ORDER BY total_revenue DESC;