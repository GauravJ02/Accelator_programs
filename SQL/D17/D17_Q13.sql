
/*
Problem Description:
The marketing division wants to identify dominant menu items that hold a high market share within their menu sections to create focused combos. 
Write a read-only SQL query to calculate the food item name, category, and total revenue pool for successfully processed rows. Use an advanced 
correlated subquery inside the HAVING clause to filter the final dataset to show only those individual food items whose cumulative sales account 
for more than 35% of the entire revenue generated within that product's parent menu category.


case=1
output=
food_item_name	category	item_total_revenue
Chicken Biryani	Main Course	900.00
Masala Dosa	Breakfast	600.00
Mango Lassi	Beverages	360.00
Gulab Jamun	Desserts	350.00
Samosa	Snacks	270.00
Butter Naan	Breads	240.00



*/
use fs;

SELECT
    fi.name AS food_item_name,
    fi.category,
    SUM(o.total_amount) AS item_total_revenue
FROM Orders o
JOIN FoodItems fi
    ON fi.food_id = o.food_id 
WHERE o.status <> 'Cancelled'
GROUP BY    
    fi.name,
    fi.category
HAVING SUM(o.total_amount) > (SELECT 0.35 * SUM(o1.total_amount) FROM Orders o1 JOIN FoodItems fi1 ON o1.food_id = fi1.food_id WHERE fi.category = fi1.category AND o1.status <> 'Cancelled')
ORDER BY item_total_revenue DESC;