"""
Problem Title:Smart Weather Time-Series Analyzer using Pandas

Problem Statement:
A meteorological department records the daily temperature of a city in a CSV file.

The weather analysts want to perform time-series analysis using Pandas.

Each weather record contains:
Date
City
Temperature

The program should perform the following operations.

Step 1:Load the weather dataset using Pandas.
Step 2:Convert the Date column into Datetime format.
Step 3:Set the Date column as DatetimeIndex.
Step 4:Display the complete weather dataset.
Step 5:Display all weather records for January.
Step 6:Display the average temperature recorded during January.

Requirements
------------
1. Read weather.csv.
2. Use pd.to_datetime().
3. Use DatetimeIndex.
4. Filter January records.
5. Calculate January average temperature.

Input File
----------
weather.csv

Output Format
-------------
Weather Dataset
...
January Weather Records
...
Average January Temperature
...

Sample weather.csv
------------------
Date,City,Temperature
2025-01-01,Hyderabad,28
2025-01-05,Hyderabad,30
2025-01-15,Hyderabad,29
2025-02-01,Hyderabad,31
2025-02-12,Hyderabad,32

Sample Output
-------------
Weather Dataset

2025-01-01 Hyderabad 28
2025-01-05 Hyderabad 30
2025-01-15 Hyderabad 29
2025-02-01 Hyderabad 31
2025-02-12 Hyderabad 32

January Weather Records

2025-01-01 Hyderabad 28
2025-01-05 Hyderabad 30
2025-01-15 Hyderabad 29

Average January Temperature
29.0
"""
import pandas as pd

weather = pd.read_csv("weather.csv")
pd.set_option('display.max_columns', None)
weather["Date"] = pd.to_datetime(weather["Date"])
weather = weather.set_index("Date")

print("Weather Dataset","\n")
print(weather.to_string(header=False,index_names=False),"\n")

print("January Weather Records","\n")
jan_data = weather.loc["2025-01"]
print(jan_data.to_string(header=False,index_names=False),"\n")

print("Average January Temperature")
avg = jan_data["Temperature"].mean()
print(avg)