"""

Problem Statement:

An e-commerce company wants to recommend the best products
to its customers based on customer ratings.

Each product record contains:

Product ID
Product Name
Product Price
Customer Rating

The product price may be either an integer or a
floating-point value.

The recommendation system evaluates products using two
different methods.

Method 1:
Find the highest rated product using a traditional
for loop.

Method 2:
Find the highest rated product using Python's built-in
max() function.

Instead of measuring execution time, compare the
performance by counting the number of operations
performed by each method.

Store all product records using a dictionary where

Product ID → (Product Name, Product Price, Rating)

The functions should use Python Type Hints.

The product price should use Union[int, float].

After processing all products:

• Display products sorted in descending order of rating.

• Display the highest rated product using both methods.

• Display the number of operations performed by each method.

• Display the better performing method.

Requirements:
-------------
1. Store product records using a dictionary.
2. Use Python Type Hints.
3. Use Union[int, float].
4. Implement Method 1 using a for loop.
5. Implement Method 2 using max().
6. Sort products using a lambda expression.
7. Count the number of operations.
8. Display the better performing method.

Input Format:
-------------
First line contains the number of products N.

Next N sets contain:

Product ID
Product Name
Product Price
Customer Rating

Output Format:
--------------
Recommended Products:

P101 -> Laptop -> 65000 -> 4.9
P103 -> Camera -> 35000 -> 4.8
P102 -> Mobile -> 25000 -> 4.5

Method 1 Highest Rating : 4.9

Method 2 Highest Rating : 4.9

Method 1 Operations : 3

Method 2 Operations : 1

Better Performing Method : Method 2

Sample Input:
-------------
3
P101
Laptop
65000
4.9
P102
Mobile
25000
4.5
P103
Camera
35000
4.8

Sample Output:
--------------
Recommended Products:
P101 -> Laptop -> 65000 -> 4.9
P103 -> Camera -> 35000 -> 4.8
P102 -> Mobile -> 25000 -> 4.5

Method 1 Highest Rating : 4.9

Method 2 Highest Rating : 4.9

Method 1 Operations : 3

Method 2 Operations : 1

Better Performing Method : Method 2

Test Cases:
-----------

case=1
input=
3
P101
Laptop
65000
4.9
P102
Mobile
25000
4.5
P103
Camera
35000
4.8

output=
Recommended Products:
P101 -> Laptop -> 65000 -> 4.9
P103 -> Camera -> 35000 -> 4.8
P102 -> Mobile -> 25000 -> 4.5

Method 1 Highest Rating : 4.9

Method 2 Highest Rating : 4.9

Method 1 Operations : 3

Method 2 Operations : 1

Better Performing Method : Method 2


case=2
input=
2
P201
Keyboard
1200
4.3
P202
Mouse
800
4.7

output=
Recommended Products:
P202 -> Mouse -> 800 -> 4.7
P201 -> Keyboard -> 1200 -> 4.3

Method 1 Highest Rating : 4.7

Method 2 Highest Rating : 4.7

Method 1 Operations : 2

Method 2 Operations : 1

Better Performing Method : Method 2


case=3
input=
1
P301
Monitor
15000
4.8

output=
Recommended Products:
P301 -> Monitor -> 15000 -> 4.8

Method 1 Highest Rating : 4.8

Method 2 Highest Rating : 4.8

Method 1 Operations : 1

Method 2 Operations : 1

Better Performing Method : Both Methods


case=4
input=
0

output=
Invalid Number of Products


case=5
input=
2
P401
Printer
12000
4.5
P402
Scanner
9000
5.5

output=
Invalid Rating
"""
from typing import Tuple, Union

def get_input():
    n = int(input())
    if n <= 0:
        raise ValueError("Invalid Number of Products")
    products = {}
    p_price: Union[int,float]
    for _ in range(n):
        p_id = input()
        p_name = input()
        p_price = input()
        c_rating = float(input())
        
        try:
            p_price = int(p_price)
        except ValueError:
            p_price = float(p_price)
        
        if not 0 <= c_rating <= 5:
            raise ValueError("Invalid Rating")
            
        products[p_id] = (p_name, p_price, c_rating)
    
    return products

class ProcessData:
    def __init__(self, data):
        self.data = data
    
    def method1(self) -> Tuple[float,int]:
        count = 0
        max_rating = -1
        for key, value in self.data.items():
            p_name, p_price, c_rating = value
            if c_rating > max_rating:
                max_rating = c_rating
            count += 1
        return max_rating,count
    
    def method2(self) -> Tuple[float, int]:
        count = 0
        max_rating = max(self.data.items(),key = lambda x:x[1][-1])
        return max_rating[1][-1], 1
    
    def display(self) -> None:
        print("Recommended Products:")
        sorted_data = sorted(self.data.items(), key = lambda x: x[1][-1], reverse = True)
        for key, value in sorted_data:
            p_name, p_price, c_rating = value
            print(f"{key} -> {p_name} -> {p_price} -> {c_rating}")
        print()
        
        rating1,count1 = self.method1()
        rating2,count2 = self.method2()
        print(f"Method 1 Highest Rating : {rating1}")
        print()
        print(f"Method 2 Highest Rating : {rating2}")
        print()
        print(f"Method 1 Operations : {count1}")
        print()
        print(f"Method 2 Operations : {count2}")
        print()
        
        if count1 == count2:
            print("Better Performing Method : Both Methods")
        elif count1 > count2:
            print("Better Performing Method : Method 2")
        else:
            print("Better Performing Method : Method 1")

def main():
    try:
        products = get_input()
        
        pd = ProcessData(products)
        
        pd.display()
    except ValueError as e:
        print(e)

main()