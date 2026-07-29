"""
A regional logistics firm operates a growing fleet of heavy-duty delivery trucks 
across multiple interstate routes to handle daily freight distribution.
Due to fluctuating diesel fuel prices, varying road topography, and regional toll 
structures, the company's operational expenses fluctuate heavily from week to week.
The fleet management team wants to establish an automated time-series monitoring 
system that tracks daily fuel usage, mileage, tolls, and regional tax surcharges 
for every active vehicle.
Vehicles that exhibit poor fuel efficiency cause disproportionate strain on company 
profits and contribute higher relative carbon emissions on long trips.
By calculating real-time mileage metrics, applying maintenance penalty surcharges to
inefficient vehicles, broadcasting regional taxes, and resampling logs into standardized
daily financial totals, management can better optimize route planning and allocate 
weekly fuel budgets accurately.

Step-by-Step Requirements
-----------------------------
1.Time-Series Ingestion: Read fleet_logs.csv into a Pandas DataFrame. 
   Convert the LogDate column to a DatetimeIndex.
2.Array Vectorization & Broadcasting:
  2.1.Extract Distance_KM, Fuel_Liters, Fuel_Price_Per_Liter, and Toll_Cost as NumPy arrays (ndarray).
  2.2.Compute Fuel Efficiency (KM/L): Distance_KM *Fuel_Liters.
  2.3.Compute Base Fuel Cost ($): Fuel_Liters *Fuel_Price_Per_Liter.
  2.4.Apply Surcharge Penalty ($): If KM/L < 4.0, apply a flat $15.00 maintenance fee; 
      otherwise, $0.00.
  2.5.Broadcast a Regional Tax Multiplier (5% tax rate, 1.05) across base fuel costs.
  2.6.Compute Total Cost ($):(Base Fuel Cost *1.05) + Toll_Cost + Surcharge Penalty.

3.Filtering & Index Slicing: Use .loc to isolate long-haul delivery runs where 
   Distance_KM}> 200.0.
   
4.Time Series Resampling: Resample data on a daily (D) frequency to sum total distance, fuel, tolls, and overall costs per date.
5.Output Generation: Output a clean DataFrame containing LogDate, Distance_KM, Fuel_Liters, Toll_Cost, and Total_Cost, with all numeric outputs formatted to 2 decimal places.


Input Format (fleet_logs.csv)
-------------------------------
LogDate,TruckID,Distance_KM,Fuel_Liters,Fuel_Price_Per_Liter,Toll_Cost
2026-08-01 08:00:00,T101,450.0,120.0,1.50,15.00
2026-08-01 10:00:00,T102,280.0,80.0,1.60,10.00
2026-08-02 09:00:00,T103,150.0,30.0,1.45,5.00
2026-08-02 11:00:00,T104,600.0,180.0,1.55,20.00


output=
--------
LogDate,Distance_KM,Fuel_Liters,Toll_Cost,Total_Cost
2026-08-01,730.00,200.00,25.00,378.40
2026-08-02,600.00,180.00,20.00,327.95





"""
import numpy as np
import pandas as pd

fleet_logs = pd.read_csv("fleet_logs.csv")

fleet_logs["LogDate"] = pd.to_datetime(fleet_logs["LogDate"])
fleet_logs = fleet_logs.set_index("LogDate")

distance = fleet_logs["Distance_KM"].to_numpy()
fuel_liters = fleet_logs["Fuel_Liters"].to_numpy()
fuel_price = fleet_logs["Fuel_Price_Per_Liter"].to_numpy()
toll_cost = fleet_logs["Toll_Cost"].to_numpy()

fuel_eff = distance/fuel_liters
base_cost = fuel_liters * fuel_price
surcharge = fuel_eff.copy()
mask = surcharge < 4
surcharge[mask] = 15
surcharge[~(mask)] = 0
#better approach use np.where(condition,True_value,False_Value)
base_cost *= 1.05
total = base_cost + surcharge + toll_cost

fleet_logs["Total_Cost"] = total.round(2)

fleet_logs = fleet_logs.loc[fleet_logs["Distance_KM"] > 200.0]
fleet_logs = fleet_logs.resample("D").sum()

print("LogDate,Distance_KM,Fuel_Liters,Toll_Cost,Total_Cost")

for i, row in fleet_logs.iterrows():
    print(f"{i.strftime('%Y-%m-%d')},{row['Distance_KM']:.2f},{row['Fuel_Liters']:.2f},{row['Toll_Cost']:.2f},{row['Total_Cost']:.2f}")
