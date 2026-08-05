/*
Problem Description:
The marketing team wants to identify which food items are completely unpopular or haven't successfully converted into delivered sales yet. 
Write an SQL query to list the names of all food items, their categories, and the total count of times they have been successfully delivered.
Use a left join to ensure that food items with zero delivered orders are still present in the list with a count of 0. Sort the results alphabetically by the food item name.

case=1
output=
food_item_name	category	total_delivered_orders
Butter Naan	Breads	2
Chicken Biryani	Main Course	1
Chole Bhature	Breakfast	1
Dal Tadka	Main Course	1
Gulab Jamun	Desserts	1
Mango Lassi	Beverages	1
Masala Dosa	Breakfast	1
Paneer Butter Masala	Main Course	0
Samosa	Snacks	2
Veg Fried Rice	Main Course	1

*/
use fs;

SELECT fi.name food_item_name, fi.category category, COUNT(o.order_id) total_delivered_orders
FROM FoodItems fi LEFT JOIN Orders o 
    ON o.food_id = fi.food_id AND o.status = "Delivered"
GROUP BY fi.name, fi.category
ORDER BY food_item_name;