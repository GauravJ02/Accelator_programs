/*
Problem : 
The finance team needs a breakdown showing how much revenue each food item 
contributes relative to its entire menu category. Use windowed aggregation SUM() 
OVER(PARTITION BY category) inside a CTE to compute the total category sales and 
calculate each food item's exact percentage contribution to its category revenue.

case=1
output=
category	food_name	item_revenue	category_total_revenue	revenue_pct
Beverages	Mango Lassi	360.00	360.00	100.00
Breads	Butter Naan	240.00	240.00	100.00
Breakfast	Masala Dosa	600.00	900.00	66.67
Breakfast	Chole Bhature	300.00	900.00	33.33
Desserts	Gulab Jamun	350.00	350.00	100.00
Main Course	Chicken Biryani	900.00	2090.00	43.06
Main Course	Paneer Butter Masala	500.00	2090.00	23.92
Main Course	Veg Fried Rice	390.00	2090.00	18.66
Main Course	Dal Tadka	300.00	2090.00	14.35
Snacks	Samosa	270.00	270.00	100.00
*/
use fs;

WITH item_rev AS (
    SELECT fi.category, fi.name AS food_name,
           SUM(o.total_amount) AS item_revenue
    FROM Orders o
    JOIN FoodItems fi ON o.food_id = fi.food_id
    GROUP BY fi.category, fi.name
),
cat_rev AS (
    SELECT category, food_name, item_revenue,
           SUM(item_revenue) OVER (PARTITION BY category) AS category_total_revenue
    FROM item_rev
)
SELECT category, food_name, item_revenue, category_total_revenue,
       ROUND(item_revenue / category_total_revenue * 100, 2) AS revenue_pct
FROM cat_rev
ORDER BY category, item_revenue DESC;