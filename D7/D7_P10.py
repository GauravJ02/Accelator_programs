"""

Problem Statement:

An electric vehicle manufacturer wants to analyze the
battery health of multiple electric vehicles.

Each vehicle contains battery cells.

The voltage of every battery cell is stored using
a NumPy matrix.

Each row represents one vehicle.

Each column represents one battery cell.

A healthy battery cell should have voltage between 3.5V and 4.2V.

The Battery Management System (BMS) performs the following analysis.

Step 1
Identify weak battery cells.
Voltage < 3.5V

Step 2
Identify overcharged battery cells.
Voltage > 4.2V

Step 3
Normalize all voltages.
If voltage < 3.5
set voltage = 3.5
If voltage > 4.2
set voltage = 4.2

Use NumPy clip().

Step 4
Calculate Battery Health Score.

Health Score=(Normal Cells / Total Cells)×100

Step 5

Classify battery condition.
Health Score >=95
Excellent
Health Score >=80
Good
Otherwise
Poor

The entire analysis should be performed using
• NumPy Arrays
• Broadcasting
• Boolean Masking
• Vectorization
• np.where()
• np.clip()

Requirements
------------
1 Store voltages in NumPy matrix.
2 Use reshape().
3 Use Boolean Masking.
4 Use np.where().
5 Use np.clip().
6 Display Weak Cells.
7 Display Overcharged Cells.
8 Display Normalized Matrix.
9 Display Health Score.
10 Display Battery Status.

Input Format
---------------
Number of Vehicles
Number of Battery Cells
Voltage values

Output Format
--------------
Weak Cells : <count>
Overcharged Cells : <count>
Normalized Battery Matrix
....
Battery Health Score : xx.xx
Battery Status : Excellent


Sample Input:
-------------
2
4
3.6
3.4
4.3
4.0
3.8
3.5
4.1
4.4
Sample Output
-----------------
Weak Cells : 1
Overcharged Cells : 2
Normalized Battery Matrix:
3.6 3.5 4.2 4.0
3.8 3.5 4.1 4.2

Battery Health Score : 62.5

Battery Status : Poor


Explanation:
-------------
Weak Cells = 3.4 → 1 cell
Overcharged Cells = 4.3, 4.4 → 2 cells
Healthy Cells = 3.6, 4.0, 3.8, 3.5, 4.1 → 5 cells
Total Cells = 8
Health Score = (5 / 8) × 100 = 62.5
Status = Poor

Test Cases
----------

case=1
input=
2
4
3.6
3.4
4.3
4.0
3.8
3.5
4.1
4.4
output=
Weak Cells : 1
Overcharged Cells : 2
Normalized Battery Matrix:
3.6 3.5 4.2 4.0
3.8 3.5 4.1 4.2

Battery Health Score : 62.5
Battery Status : Poor


case=2
input=
2
3
3.6
3.8
4.0
3.7
3.9
4.1
output=
Weak Cells : 0
Overcharged Cells : 0
Normalized Battery Matrix:
3.6 3.8 4.0
3.7 3.9 4.1

Battery Health Score : 100.0
Battery Status : Excellent


case=3
input=
3
2
3.4
3.5
4.1
4.3
3.8
3.9
output=
Weak Cells : 1
Overcharged Cells : 1
Normalized Battery Matrix:
3.5 3.5
4.1 4.2
3.8 3.9

Battery Health Score : 66.67
Battery Status : Poor


case=4
input=
0
output=
Invalid Number of Vehicles


case=5
input=
2
2
3.6
-1
3.8
4.0
output=
Invalid Battery Voltage
"""
import numpy as np

def get_input():
    n = int(input())
    if n <= 0:
        raise ValueError("Invalid Number of Vehicles")
        
    v = int(input())
    battery = [float(input()) for _ in range(n*v)]
    for i in battery:
        if i < 0 :
            raise ValueError("Invalid Battery Voltage")
    
    return np.array(battery).reshape(n,v)

class BMS:
    def __init__(self,battery):
        self.battery = battery
    
    def weak_cells(self):
        weak = self.battery >= 3.5
        return weak.size - weak.sum()
    
    def over_charged(self):
        overcharged = self.battery <= 4.2
        return overcharged.size - overcharged.sum()
    
    def normalize(self):
        return self.battery.clip(3.5,4.2)
    
    def health_score(self):
        normal_cells = np.where((self.battery >= 3.5) & (self.battery <= 4.2), 1,0)
        normal = normal_cells.sum()
        total = normal_cells.size
        health_score = (normal/total) * 100
        return round(health_score,2)
    
    def status(self):
        health = self.health_score()
        if health >= 95:
            return "Excellent"
        elif health >= 80:
            return "Good"
        else:
            return "Poor"
    
    def display(self):
        print(f"Weak Cells : {self.weak_cells()}")
        print(f"Overcharged Cells : {self.over_charged()}")
        print("Normalized Battery Matrix:")
        normal = self.normalize()
        for i in normal:
            print(*i)
        print()
        print(f"Battery Health Score : {self.health_score()}")
        print(f"Battery Status : {self.status()}")

def main():
    try:
        battery = get_input()
        bms = BMS(battery)
        bms.display()
    except ValueError as e:
        print(e)

main()