/*

Problem Description:
The inventory supervisor wants to calculate delivery patterns specifically for accompaniment menu categories like 'Breads' to prepare the kitchen prep list. 
Write an SQL query to retrieve the food item name, its category, and the total number of individual orders placed for that item. 
Filter the system to only look at food items categorized under 'Breads' that have a status of 'Delivered'.

case=1
output=
food_item_name	category	total_successful_orders
Butter Naan	Breads	2



*/

use fs;

SELECT
    fi.name AS food_item_name,
    fi.category,
    COUNT(o.order_id) AS total_successful_orders
FROM FoodItems fi
JOIN Orders o
    ON fi.food_id = o.food_id
WHERE fi.category = "Breads"
    AND o.status = "Delivered"
GROUP BY 
    fi.name,
    fi.category;