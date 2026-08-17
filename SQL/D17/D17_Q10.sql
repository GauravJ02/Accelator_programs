/*
Problem Description:
The kitchen inventory control office wants to identify menu choices that haven't registered any successful order fulfillments to optimize stocking space. 
Write a read-only SQL query to find the food ID, item name, category, and price of items inside the FoodItems table whose food_id is entirely absent from
transactional records currently flagged with a status of 'Delivered'.  

case=1
output=

food_id	name	category	price
1	Paneer Butter Masala	Main Course	250.00


*/
use fs;

SELECT
    fi.food_id,
    fi.name,
    fi.category,
    fi.price
FROM FoodItems fi
LEFT JOIN Orders o
    ON fi.food_id = o.food_id AND o.status = 'Delivered'
WHERE o.food_id IS NULL;