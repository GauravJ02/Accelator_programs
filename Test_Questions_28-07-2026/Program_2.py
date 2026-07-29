"""
A rapidly growing retail enterprise operates multiple brick-and-mortar store branches 
across various geographical regions. To keep operational overhead low, raw 
transactional records and store metadata are managed in separate software platforms,
resulting in disconnected datasets.

At the end of each sales cycle, executives need a consolidated report showing revenue 
across product categories, but only for verified and completed sales. Cancelled 
transactions and micro-purchases under $80.00 skew overall regional averages and must 
be removed prior to computing financial metrics.

By integrating transaction logs with store profiles, filtering out unverified or 
low-value sales, and calculating grouped total and average sales, leadership can make 
informed stock distribution decisions.


Requirements:
-----------------
1.Load Datasets: Read transactions.csv and store_info.csv.

2.Data Integration: Perform an inner join on StoreID.

3.Filtering: Use .loc to retain transactions where Status == 'Completed' and Amount >= 80.0.

4.Data Aggregation: Group by Region and Category. Compute:

    Total_Sales: Sum of Amount

    Avg_Sales: Mean of Amount

5.Formatting: Sort by Region and Category alphabetically. Format all aggregated financial values strictly to two decimal places (including trailing zeros, e.g., 80.00, 770.00).

Input Format: 
-------------
transactions.csv
---------------
TxnID,StoreID,Category,Amount,Status
TX101,S1,Electronics,250.0,Completed
TX102,S2,Apparel,80.0,Completed
TX103,S1,Electronics,400.0,Completed
TX104,S3,Apparel,150.0,Cancelled
TX105,S2,Electronics,120.0,Completed

store_info.csv
----------------
StoreID,StoreName,Region
S1,Downtown Megastore,North
S2,Suburban Plaza,North
S3,Metro Center,South


Output Format
----------------
Region,Category,Total_Sales,Avg_Sales
North,Apparel,80.00,80.00
North,Electronics,770.00,256.67

"""
import pandas as pd

tran = pd.read_csv("transactions.csv")
store_info = pd.read_csv("store_info.csv")

merged = tran.merge(store_info,on="StoreID",validate="many_to_one")

merged = merged.loc[(merged["Status"]=="Completed") & (merged["Amount"] >= 80.0)]

merged = merged.groupby(["Region","Category"]).agg(Total_Sales=("Amount","sum"), Avg_Sales=("Amount","mean")).reset_index()

merged.sort_values("Region").sort_values("Category")

print("Region,Category,Total_Sales,Avg_Sales")
for i, row in merged.iterrows():
    print(f"{row['Region']},{row['Category']},{row['Total_Sales']:.2f},{row['Avg_Sales']:.2f}")