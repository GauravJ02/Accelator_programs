"""
Project Title: Smart Hospital Patient Data Cleansing and Healthcare Intelligence Platform using NumPy and Pandas

Problem Statement:
A multi-specialty hospital maintains patient information in multiple CSV files.
Patient records are collected from different hospital branches. During synchronization, 
some records contain missing values, duplicate entries, and inconsistent treatment information.
Before generating analytical reports, the hospital management wants to clean the data and 
generate a Healthcare Intelligence Dashboard.

The available CSV files are:
Patient File Contains
Patient ID
Patient Name
Department
Age

Treatment File Contains
Patient ID
Consultation Cost
Lab Cost
Pharmacy Cost

Billing File Contains
Patient ID
Admission Date
Total Bill

Vitals File Contains
    Patient ID
    Blood Pressure
 Some records contain
    Missing Treatment Costs
    Missing Blood Pressure
    Duplicate Patient Records

The program should perform the following operations.
Step 1:Load all four CSV files using Pandas.
Step 2:Merge all DataFrames using Patient ID.
Step 3: Display the complete merged dataset.
Step 4:Display missing values using isnull().
Step 5:Fill missing Total Bill using the average bill of all patients using fillna().
Step 6:Recover missing Blood Pressure using interpolate().
Step 7:Remove duplicate patient records using drop_duplicates().
Step 8:Convert Admission Date into Datetime using pd.to_datetime().
Step 9:Set Admission Date as DatetimeIndex.
Step 10:Generate Monthly Hospital Revenue using resample().
Step 11:Generate Department-wise Revenue using groupby().
Step 12:Generate a Department-wise Revenue Pivot Table using pivot_table().
Step 13:Convert Treatment Columns
Consultation Cost
Lab Cost
Pharmacy Cost
into Long Format using melt().

Step 14:Reconstruct the original treatment table using pivot().
Step 15:Using loc() Display only Cardiology patients.
Step 16:Using iloc() Display second and third patient records.
Step 17: Using NumPy Vectorization
Calculate
Insurance Bonus
Insurance Bonus = Total Bill × 5%

Step 18:Using NumPy Broadcasting
Calculate:Final Bill = Total Bill + Insurance Bonus

Step 19:Display the department generating the highest revenue.

Step 20:Display the patient having the highest bill.

Requirements:
----------------
Read four CSV files.
Merge multiple DataFrames.
Use isnull().
Use fillna().
Use interpolate().
Use drop_duplicates().
Use pd.to_datetime().
Use DatetimeIndex.
Use resample().
Use groupby().
Use pivot_table().
Use melt().
Use pivot().
Use loc().
Use iloc().
Use NumPy Arrays.
Use Vectorization.
Use Broadcasting.


Input Files:
--------------
patients.csv
----------
PatientID,PatientName,Department,Age
P101,Ravi,Cardiology,45
P102,Priya,Neurology,38
P103,Rahul,Orthopedics,50
P104,Anu,Cardiology,42
P105,Kiran,Neurology,36
P105,Kiran,Neurology,36

Note: Last record is intentionally duplicated.
It will be removed using drop_duplicates().

treatments.csv
--------------
PatientID,ConsultationCost,LabCost,PharmacyCost
P101,500,1200,800
P102,600,1000,900
P103,550,1500,1000
P104,650,1100,850
P105,500,1300,950



billing.csv
--------------
PatientID,AdmissionDate,TotalBill
P101,2025-01-05,25000
P102,2025-01-18,
P103,2025-02-10,32000
P104,2025-02-20,28000
P105,2025-03-08,

Note:Missing bills for
P102
P105
These must be filled

vitals.csv
--------------
PatientID,BloodPressure
P101,120
P102,
P103,130
P104,
P105,125

Missing Blood Pressure:
P102
P104
These will be recovered 


case=1
output=
Complete Hospital Report
P101 Ravi Cardiology 45 500 1200 800 2025-01-05 25000.0 120.0
P102 Priya Neurology 38 600 1000 900 2025-01-18 nan nan
P103 Rahul Orthopedics 50 550 1500 1000 2025-02-10 32000.0 130.0
P104 Anu Cardiology 42 650 1100 850 2025-02-20 28000.0 nan
P105 Kiran Neurology 36 500 1300 950 2025-03-08 nan 125.0
P105 Kiran Neurology 36 500 1300 950 2025-03-08 nan 125.0

Missing Values
False False False False False False False False False False
False False False False False False False False True True
False False False False False False False False False False
False False False False False False False False False True
False False False False False False False False True False
False False False False False False False False True False

Recovered Dataset
P101 Ravi Cardiology 45 25000.0 120.0
P102 Priya Neurology 38 28333.33 125.0
P103 Rahul Orthopedics 50 32000.0 130.0
P104 Anu Cardiology 42 28000.0 127.5
P105 Kiran Neurology 36 28333.33 125.0

Monthly Hospital Revenue
2025-01 53333.33
2025-02 60000.0
2025-03 28333.33

Department Revenue
Cardiology 53000.0
Neurology 56666.67
Orthopedics 32000.0

Department Revenue Pivot Table

OrderDate    2025-01  2025-02  2025-03
Department
Cardiology    25000.0   28000.0      0.0
Neurology     28333.33      0.0 28333.33
Orthopedics       0.0   32000.0      0.0

Treatment Long Format
P101 Ravi ConsultationCost 500
P102 Priya ConsultationCost 600
P103 Rahul ConsultationCost 550
P104 Anu ConsultationCost 650
P105 Kiran ConsultationCost 500
P101 Ravi LabCost 1200
P102 Priya LabCost 1000
P103 Rahul LabCost 1500
P104 Anu LabCost 1100
P105 Kiran LabCost 1300
P101 Ravi PharmacyCost 800
P102 Priya PharmacyCost 900
P103 Rahul PharmacyCost 1000
P104 Anu PharmacyCost 850
P105 Kiran PharmacyCost 950

Reconstructed Treatment Dataset

Treatment PatientID PatientName ConsultationCost LabCost PharmacyCost
0 P101 Ravi 500 1200 800
1 P102 Priya 600 1000 900
2 P103 Rahul 550 1500 1000
3 P104 Anu 650 1100 850
4 P105 Kiran 500 1300 950

Cardiology Patients
P101 Ravi 25000.0
P104 Anu 28000.0

Second and Third Patients
P102 Priya Neurology
P103 Rahul Orthopedics

Insurance Bonus
1250.0
1416.67
1600.0
1400.0
1416.67

Final Bill
26250.0
29750.0
33600.0
29400.0
29750.0

Highest Revenue Department
Neurology 56666.67

Highest Bill Patient
P103 Rahul 32000.0
"""
import numpy as np
import pandas as pd

patients = pd.read_csv("patients.csv")
treatments = pd.read_csv("treatments.csv")
billing = pd.read_csv("billing.csv")
vitals = pd.read_csv("vitals.csv")

merged = patients.merge(treatments, on="PatientID").merge(billing, on="PatientID").merge(vitals, on="PatientID")
print("Complete Hospital Report")
print(merged.to_string(index=False,header=False),"\n")

print("Missing Values")
print(merged.isnull().to_string(index=False,header=False),"\n")

print("Recovered Dataset")
average_bill = merged["TotalBill"].mean()
recovered_data = merged["TotalBill"].fillna(average_bill)
recovered_data["BloodPressure"] = merged["BloodPressure"].interpolate()
recovered_data = recovered_data.drop_duplicates(subset=["PatientID"])
print(recovered_data[["PatientID","PatientName","Department","Age","TotalBill","BloodPressure"]].to_string(index=False,header=False),"\n")
