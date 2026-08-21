/*
Problem : Category Product Launch Pioneer

The food platform operation team is analyzing product launch performance 
across different culinary categories. For each category (e.g., Main Course, Breakfast, Snacks), 
they need to identify the very first item ordered historically on the platform. 
This will help assess initial category traction and order timing patterns.

case=1
output=
order_id	category	food_item	order_date
20	Beverages	Mango Lassi	2026-06-17 11:17:55
3	Breads	Butter Naan	2026-06-17 11:17:55
4	Breakfast	Masala Dosa	2026-06-17 11:17:55
2	Desserts	Gulab Jamun	2026-06-17 11:17:55
11	Main Course	Chicken Biryani	2026-06-17 11:17:55
15	Snacks	Samosa	2026-06-17 11:17:55



*/
use fs;

WITH ranking AS(
    SELECT
    o.order_id,
    fi.category,
    fi.name AS food_item,
    o.order_date,
    ROW_NUMBER() OVER(PARTITION BY fi.category ORDER BY o.order_date) AS rnk
    FROM Orders o
    JOIN FoodItems fi 
        ON o.food_id = fi.food_id
)
SELECT order_id, category, food_item, order_date FROM ranking
WHERE rnk = 1
ORDER BY category;
