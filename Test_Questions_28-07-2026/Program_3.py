"""

Problem statement:
------------------
An environmental protection agency monitors automated climate telemetry from IoT 
sensors stationed across multiple smart cities.
Sensor streams transmit readings in an unpivoted wide format, grouping morning and 
evening temperature and humidity parameters into dynamic columns.

To conduct climate change assessments and trigger heat wave alerts, the agency requires 
a data processing pipeline.

The system must unpivot the raw sensor data, reconstruct normalized time-stamped 
records, compute combined heat indices using multi-dimensional array operations, 
resample readings over specific time windows using DatetimeIndex, and isolate severe 
environmental anomalies.

Requirements
--------------
1.Unpivot / Melt Data:
  Read sensor_logs.csv. Unpivot wide columns (Morning_Temp, Evening_Temp, 
  Morning_Hum, Evening_Hum) into standard long-format rows.
2.String Extraction & Reshaping:Split metric names into TimeOfDay(Morning / Evening) 
  and Measurement (Temp / Hum). Pivot back to generate distinct Temp and Hum columns.
3.Time Series Indexing & Resampling:Combine Date and TimeOfDay into a timestamp column,
  convert to DatetimeIndex, and apply resample('12H').
4.Multi-Dimensional Array Operations & Broadcasting:
  Extract temperature and humidity columns as 2D ndarray shapes. 
  Perform vectorized heat index calculation:      HeatIndex=Temp+ (0.55 * Hum)
5.Merging & Filtering:Merge city demographic metadata from city_info.csv on City.
  Use .loc to filter records where HeatIndex > 65.0. Use .iloc for final indexing.


CSV Inputs
-----------
File 1: sensor_logs.csv
------------------------
City,Date,Morning_Temp,Evening_Temp,Morning_Hum,Evening_Hum
Austin,2026-08-01,32,38,70,50
Austin,2026-08-02,28,30,40,45
Seattle,2026-08-01,20,22,60,65

File 2: city_info.csv
-----------------------
City,State,Zone
Austin,Texas,South
Seattle,Washington,North

Expected Output
----------------
Timestamp,City,Zone,Temp,Hum,HeatIndex
2026-08-01 08:00:00,Austin,South,32.0,70.0,70.5
2026-08-01 20:00:00,Austin,South,38.0,50.0,65.5
"""
import numpy as np
import pandas as pd

sensor = pd.read_csv("sensor_logs.csv")
city_info = pd.read_csv("city_info.csv")
sensor = sensor.merge(city_info,on="City")

sensor = sensor.melt(id_vars=["City","Date","Zone"],value_vars=["Morning_Temp","Evening_Temp","Morning_Hum","Evening_Hum"], var_name="Metric",value_name="Data").reset_index()

sensor[["TimeOfDay","Measurement"]] = sensor["Metric"].str.split("_",expand=True)

sensor = sensor.pivot(values="Data",index=["City","Date","Zone","TimeOfDay"],columns="Measurement").reset_index()

sensor["TimeOfDay"] = sensor["TimeOfDay"].map({
    "Morning": "08:00:00",
    "Evening": "20:00:00"
})

sensor["Timestamp"] = sensor["Date"]+" "+sensor["TimeOfDay"]
sensor["Timestamp"] = pd.to_datetime(sensor["Timestamp"])
sensor = sensor.set_index("Timestamp")
sensor = sensor.groupby("City").resample("12H",origin="start").first().reset_index(level=0,drop=True)

hum = sensor[["Hum"]].to_numpy()
Temp = sensor[["Temp"]].to_numpy()
sensor["HeatIndex"] = (Temp + (0.55*hum)).ravel()
sensor = sensor.loc[sensor["HeatIndex"] > 65.0]
print("Timestamp,City,Zone,Temp,Hum,HeatIndex")

for i, row in sensor.iterrows():
    print(f"{i},{row['City']},{row['Zone']},{row['Temp']},{row['Hum']},{row['HeatIndex']}")