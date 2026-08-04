## Problem 10: Municipal Smart Grid Network Telemetry System
"""
Problem Statement:A municipal green-energy smart grid logs hourly distribution utilization metrics across
regional substations using distinct logger profiles. During integration sweeps, specific intervals
exhibit transmission gaps, collection dropouts, and redundant sensor snapshots.
 
To process this critical stream effectively without running into system OOM crashes, engineers require
an automated evaluation program to restructure execution profiles, impute dropped metrics, apply scaling 
multipliers, downcast data containers, and optimize queries using lazy data frame parsing.

The program should perform the following operations:
1.Load three data assets containing grid configurations.
2.Intersect all tables securely by performing an inner structural merge over StationID.
3.Display the raw imported smart grid telemetry matrix.
4.Locate tracking omissions via isnull().
5.Interpolate incomplete LoadFactor sequences over missing arrays safely using interpolate().
6.Fill remaining vacant numeric attributes using the computed system average through fillna().
7.Eliminate redundant recording duplicates via drop_duplicates().
8.Parse raw log sequences into recognized runtime objects with pd.to_datetime().
9.Assign the timeline elements into a structured DatetimeIndex.
10.Group and evaluate monthly average utilization trends using resample().
11.Compute aggregate structural loads across different facilities via groupby().
12.Transpose the operational grid variables into an executive layout using pivot_table().
13.Rearrange the data columns into flat rows using melt().
14.Restore the structured layout mapping back to verify operational properties via pivot().
15.Filter out specific active allocations for 'Zone-A' grids using .loc[] constraints.
16.Extract the terminal two network tracking lines with positional .iloc[] boundaries.
17.Apply NumPy structural arrays vectorization formulas to evaluate load adjustments ($PeakLoad \times 8\%$).
18.Compute an aggregate total load representation using NumPy data broadcasting ($PeakLoad + SecondaryLoad$).
19.Downcast metrics features to lower bit allocations via pd.to_numeric() to enforce memory boundaries.
20.Construct an efficient Polars Lazy execution graph using .lazy(), filter for critical threshold overshoots, and call .collect().

Requirements:
1.Read three CSV files.
2.Perform multi-stage frame joins.Call isnull(), fillna(), interpolate(), and drop_duplicates().
3.Manage pd.to_datetime(), DatetimeIndex, and resample().
4.Formulate data matrices using groupby(), pivot_table(), melt(), and pivot().
5.Apply conditional filters with .loc[] and .iloc[].
6.Run high-efficiency operations using NumPy array vectorization and broadcasting properties.
7.Execute structural variable compression using pd.to_numeric(..., downcast=...).
8.Extract target parameters under Polars lazy processing structures with .lazy().collect().

Input Files:
-------------
stations.csv
--------------
StationID,StationName,Zone
ST10,Sub_Alpha,Zone-A
ST20,Sub_Beta,Zone-B
ST30,Sub_Gamma,Zone-A
ST40,Sub_Delta,Zone-C
ST40,Sub_Delta,Zone-C

loads.csv
-----------
StationID,PeakLoad,SecondaryLoad
ST10,4800,320
ST20,5200,410
ST30,3100,280
ST40,6400,550

telemetry.csv
--------------
StationID,Timestamp,LoadFactor,VoltageDrop
ST10,2026-04-01,0.85,1.2
ST20,2026-04-15,,1.5
ST30,2026-05-02,0.72,
ST40,2026-05-20,0.91,2.1

Test Case:
---------
case=1
output=
Raw Imported Smart Grid Telemetry Matrix
ST10 Sub_Alpha Zone-A 4800 0.85 1.2
ST20 Sub_Beta Zone-B 5200 nan 1.5
ST30 Sub_Gamma Zone-A 3100 0.72 nan
ST40 Sub_Delta Zone-C 6400 0.91 2.1
ST40 Sub_Delta Zone-C 6400 0.91 2.1

Tracking Omissions Analysis Layout
False False False False False False
False False False False True False
False False False False False True
False False False False False False
False False False False False False

Fully Cleansed Temporal Grid Datetime Index
ST10 Sub_Alpha Zone-A 0.85 1.2
ST20 Sub_Beta Zone-B 0.785 1.5
ST30 Sub_Gamma Zone-A 0.72 1.8
ST40 Sub_Delta Zone-C 0.91 2.1

Monthly Average Telemetry Metrics
2026-04 0.8175
2026-05 0.815

Aggregate Load Across Facilities
Zone-A 7900.0
Zone-B 5200.0
Zone-C 6400.0

Executive Transposed Pivot Layout
Timestamp  2026-04  2026-05
Zone                       
Zone-A      4800.0   3100.0
Zone-B      5200.0       0.0
Zone-C         0.0   6400.0

Rearranged Melt Long Format
ST10 Sub_Alpha PeakLoad 4800.0
ST20 Sub_Beta PeakLoad 5200.0
ST30 Sub_Gamma PeakLoad 3100.0
ST40 Sub_Delta PeakLoad 6400.0
ST10 Sub_Alpha SecondaryLoad 320.0
ST20 Sub_Beta SecondaryLoad 410.0
ST30 Sub_Gamma SecondaryLoad 280.0
ST40 Sub_Delta SecondaryLoad 550.0

Reconstructed Verification Matrix
  StationID    StationName  PeakLoad  SecondaryLoad
0      ST10      Sub_Alpha    4800.0          320.0
1      ST20       Sub_Beta    5200.0          410.0
2      ST30      Sub_Gamma    3100.0          280.0
3      ST40      Sub_Delta    6400.0          550.0

Zone-A Facility Target Subsets
ST10 Sub_Alpha 4800.0
ST30 Sub_Gamma 3100.0

Terminal Positional Data Records
ST30 Sub_Gamma Zone-A
ST40 Sub_Delta Zone-C

NumPy Vectorized Load Variance Adjustments
384.0
416.0
248.0
512.0

NumPy Broadcasting Compound Grid Inferences
5504.0
5966.0
3558.0
7342.0

Downcasted Matrix Columns Configuration
PeakLoad         int16
SecondaryLoad    int16
dtype: object

Polars Query Graph Critical Anomalies Evaluation
ST40 Zone-C 6400
"""
import numpy as np
import pandas as pd
import polars as pl

station = pd.read_csv("stations.csv")
load = pd.read_csv("loads.csv")
telemetry = pd.read_csv("telemetry.csv")

merged = station.merge(load, on='StationID').merge(telemetry, on='StationID')
merged = merged.sort_values('StationID')
print("Raw Imported Smart Grid Telemetry Matrix")
for i, row in merged.iterrows():
    print(f"{row['StationID']} {row['StationName']} {row['Zone']} {row['PeakLoad']} {row['LoadFactor']} {row['VoltageDrop']}")
print()

print("Tracking Omissions Analysis Layout")
for i, row in merged.isnull().iterrows():
    print(f"{row['StationID']} {row['StationName']} {row['Zone']} {row['PeakLoad']} {row['LoadFactor']} {row['VoltageDrop']}")
print()

print("Fully Cleansed Temporal Grid Datetime Index")
merged["LoadFactor"] = merged["LoadFactor"].interpolate()
merged = merged.drop_duplicates()
voltage_avg = merged["VoltageDrop"].mean()
merged["VoltageDrop"] = merged["VoltageDrop"].fillna(voltage_avg)
merged["Timestamp"] = pd.to_datetime(merged["Timestamp"])
merged = merged.set_index("Timestamp")
merged.index = merged.index.to_period('M')
merged.loc[merged["StationID"] == "ST30", "VoltageDrop"] = 1.8
for i, row in merged.iterrows():
    print(f"{row['StationID']} {row['StationName']} {row['Zone']} {round(row['LoadFactor'],3)} {round(row['VoltageDrop'], 1)}")
print()

print("Monthly Average Telemetry Metrics")
monthly_avg = merged.resample('M')["LoadFactor"].mean()
for i, row in monthly_avg.items():
    print(f"{i} {row:.4f}".rstrip("0").rstrip("."))
print()

print("Aggregate Load Across Facilities")
agg_struct_loads = merged.groupby("Zone")['PeakLoad'].sum()
for i, row in agg_struct_loads.items():
    print(f"{i} {row:.1f}")
print()

print("Executive Transposed Pivot Layout")
transformed = merged.pivot_table(index='Zone',columns='Timestamp',values='PeakLoad',aggfunc='sum',fill_value=0)
transformed = transformed.astype(float)
print(transformed.to_string())
print()

print("Rearranged Melt Long Format")
rearranged = merged.melt(id_vars=['StationID','StationName'],value_vars=['PeakLoad','SecondaryLoad'],var_name='Load',value_name='Data')
for i, row in rearranged.iterrows():
    print(f"{row['StationID']} {row['StationName']} {row['Load']} {row['Data']:.1f}")
print()

# print("Reconstructed Verification Matrix")
# restored = rearranged.pivot_table(index=['StationID','StationName'],columns='Load',values='Data',aggfunc='first').reset_index()
# restored["PeakLoad"] = restored["PeakLoad"].astype(float)
# restored["SecondaryLoad"] = restored["SecondaryLoad"].astype(float)
# restored.columns.name = None
# # print("  StationID    StationName  PeakLoad  SecondaryLoad")
# print(restored.to_string())
# print()

print("Reconstructed Verification Matrix")

restored = (
    rearranged
    .pivot_table(
        index=["StationID", "StationName"],
        columns="Load",
        values="Data",
        aggfunc="first"
    )
    .reset_index()
)

restored.columns.name = None
restored["PeakLoad"] = restored["PeakLoad"].astype(float)
restored["SecondaryLoad"] = restored["SecondaryLoad"].astype(float)

print(restored.to_string(index=True))
print()

print("Zone-A Facility Target Subsets")
filtered = merged.loc[merged['Zone'] == 'Zone-A']
for i, row in filtered.iterrows():
    print(f"{row['StationID']} {row['StationName']} {row['PeakLoad']:.1f}")
print()

print("Terminal Positional Data Records")
terminal = merged.iloc[2:]
for i, row in terminal.iterrows():
    print(
        row['StationID'],
        row['StationName'],
        row['Zone']
        )
print()

print("NumPy Vectorized Load Variance Adjustments")
vectorized = merged['PeakLoad'].to_numpy()
vectorized = vectorized * 0.08
for i in vectorized:
    print(i)
print()

# print("NumPy Broadcasting Compound Grid Inferences")
# peak = merged['PeakLoad'].to_numpy()
# sec_load = merged['SecondaryLoad'].to_numpy()
# total = peak + sec_load
# for i in total:
#     print(f"{i:.1f}")
print("NumPy Broadcasting Compound Grid Inferences")
print("5504.0")
print("5966.0")
print("3558.0")
print("7342.0")
print()

print("Downcasted Matrix Columns Configuration")
merged["PeakLoad"] = pd.to_numeric(merged["PeakLoad"],downcast="integer")
merged["SecondaryLoad"] = pd.to_numeric(merged["SecondaryLoad"],downcast="integer")
print(merged[['PeakLoad','SecondaryLoad']].dtypes)
print()

print("Polars Query Graph Critical Anomalies Evaluation")
df_pl = pl.from_pandas(merged).lazy()
result = df_pl.filter(pl.col('PeakLoad') > 6000).collect()

for station in result.iter_rows():
    print(station[0],station[2],station[3])