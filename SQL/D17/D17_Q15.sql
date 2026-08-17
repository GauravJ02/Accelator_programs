/*
Problem Description:
The senior menu performance analyst wants to find high-velocity food items that consistently drive strong transactional volume within their food groups.
Write a read-only SQL query to retrieve the food item name, category, and total quantities sold across all successfully processed transactions.

Filter the output using a correlated subquery inside the HAVING clause to return only those individual food items whose cumulative quantity sold
is strictly greater than the average individual quantity ordered for any single transaction within that exact same food category.



case=1
output=
food_item_name	category	total_quantity_sold
Samosa	Snacks	9
Butter Naan	Breads	6
Masala Dosa	Breakfast	3
Dal Tadka	Main Course	2



*/
use fs;

SELECT 
    fi.name AS food_item_name,
    fi.category,
    SUM(o.quantity) AS total_quantity_sold
FROM FoodItems fi
JOIN Orders o
    ON fi.food_id = o.food_id
WHERE o.status = 'Delivered'
GROUP BY 
    fi.name,
    fi.category
HAVING SUM(o.quantity) > (SELECT AVG(o1.quantity) FROM Orders o1 JOIN FoodItems fi1 ON o1.food_id = fi1.food_id WHERE fi.category = fi1.category AND o1.status = 'Delivered')
ORDER BY total_quantity_sold DESC;