"""
Problem statement:
A regional logistics firm operates a growing fleet of heavy-duty delivery trucks 
across multiple interstate routes to handle daily freight distribution.
Due to fluctuating diesel fuel prices and varying road topography, the company's 
operational expenses fluctuate heavily from week to week.
The fleet management team wants to establish a real-time numerical monitoring system
 that tracks daily fuel usage and mileage for every active vehicle.
Vehicles that exhibit poor fuel efficiency cause disproportionate strain on company 
profits and contribute higher relative carbon emissions on long trips.
By calculating real-time mileage metrics, applying maintenance penalty surcharges to 
inefficient vehicles, and converting raw logs into standardized financial totals, 
management can better optimize route planning and allocate weekly fuel budgets 
accurately.

Step-by-Step Requirements
1.Load Data: Read fleet_logs.csv into a Pandas DataFrame.
2.Numerical Processing & Broadcasting: Convert Distance_KM, Fuel_Liters, and Fuel_Price_Per_Liter into NumPy arrays.
3.Perform Calculations:
    Fuel Efficiency (KM/L):Distance_KM/Fuel_Liters
    Base Cost ($): Fuel_Liters*Fuel_Price_Per_Liter
    Surcharge Penalty ($): If KM/L< 4.0, apply a flat $15.00 maintenance surcharge; otherwise,$0.00.
    Total Cost ($):Base Cost +Surcharge Penalty
    
4.Output Generation: Output a clean DataFrame containing TruckID, Distance_KM, \
Fuel_Liters, KML (rounded to 2 decimal places), and Total_Cost (rounded to 2 decimal places).

input:
-------
fleet_logs.csv
----------------
TruckID,Distance_KM,Fuel_Liters,Fuel_Price_Per_Liter
T101,450.0,120.0,1.50
T102,280.0,80.0,1.60
T103,150.0,30.0,1.45
T104,600.0,180.0,1.55

Output Format:
--------------
TruckID,Distance_KM,Fuel_Liters,KML,Total_Cost
T101,450.0,120.0,3.75,195.00
T102,280.0,80.0,3.50,143.00
T103,150.0,30.0,5.00,43.50
T104,600.0,180.0,3.33,294.00
"""
import numpy as np
import pandas as pd

fleet_logs = pd.read_csv("fleet_logs.csv")

distance = fleet_logs["Distance_KM"].to_numpy()
fuel_liters = fleet_logs["Fuel_Liters"].to_numpy()
fuel_price = fleet_logs["Fuel_Price_Per_Liter"].to_numpy()

fuel_eff = distance/fuel_liters
base_cost = fuel_liters * fuel_price
surcharge = fuel_eff.copy()
mask = surcharge < 4
surcharge[mask] = 15
surcharge[~(mask)] = 0
#better approach use np.where(condition,True_value,False_Value)
total = base_cost + surcharge

fleet_logs["KML"] = fuel_eff.round(2)
fleet_logs["Total_Cost"] = total.round(2)

print("TruckID,Distance_KM,Fuel_Liters,KML,Total_Cost")

for i, row in fleet_logs.iterrows():
    print(
        row["TruckID"],
        row["Distance_KM"],
        row["Fuel_Liters"],
        row["KML"],
        row["Total_Cost"]
        )

