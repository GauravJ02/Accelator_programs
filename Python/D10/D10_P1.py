    """
Problem Title: Smart Online Food Delivery Time-Series Analytics using Pandas

Problem Statement: 
An online food delivery company maintains customer orders in multiple CSV files.

The management wants to analyze daily and monthly revenue using Pandas Time-Series analysis.

Three CSV files are available.
Customer File contains:
Customer ID
Customer Name
City

Restaurant File contains:
Restaurant ID
Restaurant Name
Category

Order File contains:
Order ID
Customer ID
Restaurant ID
Order Date
Order Amount

The program should perform the following operations.

Step 1:Load all three CSV files using Pandas.
Step 2:Merge Customer and Order datasets using Customer ID.
Step 3:Merge the above result with Restaurant dataset using Restaurant ID.
Step 4:Convert Order Date into Datetime format.
Step 5:Set Order Date as DatetimeIndex.
Step 6:Display the complete order report.
Step 7:Using resample('M'),display monthly revenue.
Step 8:Display the month generating the highest revenue.

Requirements
------------
1. Read customers.csv.
2. Read restaurants.csv.
3. Read orders.csv.
4. Merge multiple DataFrames.
5. Use pd.to_datetime().
6. Use DatetimeIndex.
7. Use resample().
8. Display highest revenue month.

Input Files
-----------
customers.csv
restaurants.csv
orders.csv

Output Format
-------------
Complete Order Report
...
Monthly Revenue Report
...
Highest Revenue Month
...


customers.csv
--------------
CustomerID,CustomerName,City
C101,Ravi,Hyderabad
C102,Priya,Chennai
C103,Rahul,Bangalore
C104,Anu,Hyderabad

restaurants.csv
----------------
RestaurantID,RestaurantName,Category
R101,Paradise,Biryani
R102,Dominos,Pizza
R103,KFC,FastFood

orders.csv
------------
OrderID,CustomerID,RestaurantID,OrderDate,OrderAmount
O101,C101,R101,2025-01-05,600
O102,C102,R102,2025-01-15,900
O103,C103,R103,2025-02-02,750
O104,C104,R101,2025-02-18,850
O105,C101,R102,2025-03-10,1200


case=1
output=
Complete Order Report
O101 Ravi Hyderabad Paradise Biryani 2025-01-05 600
O102 Priya Chennai Dominos Pizza 2025-01-15 900
O103 Rahul Bangalore KFC FastFood 2025-02-02 750
O104 Anu Hyderabad Paradise Biryani 2025-02-18 850
O105 Ravi Hyderabad Dominos Pizza 2025-03-10 1200

Monthly Revenue Report
2025-01 1500
2025-02 1600
2025-03 1200

Highest Revenue Month
2025-02 1600

"""
import pandas as pd

customers = pd.read_csv("customers.csv")
restaurants = pd.read_csv("restaurants.csv")
orders = pd.read_csv("orders.csv")

print("Complete Order Report")
merged = orders.merge(customers, on="CustomerID").merge(restaurants, on="RestaurantID")
merged = merged.sort_values("OrderID")
print(merged[["OrderID","CustomerName","City","RestaurantName","Category","OrderDate","OrderAmount"]].to_string(header=False,index=False),"\n")
merged["OrderDate"] = pd.to_datetime(merged["OrderDate"])
merged = merged.set_index("OrderDate")

monthly_revenue = merged.resample("M").sum()
monthly_revenue.index = monthly_revenue.index.to_period("M")
print("Monthly Revenue Report")
print(monthly_revenue.to_string(index_names=False,header=False),"\n")

print("Highest Revenue Month")
print(monthly_revenue.idxmax().to_string(header=False,index=False), monthly_revenue.max().to_string(header=False,index=False))