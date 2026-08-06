"""
Problem Statement:

A software company maintains application logs generated
from multiple servers.

Each log entry contains:

• Log ID
• Log Level
• Module Name

The Log Level can be one of the following:

INFO
WARNING
ERROR

The system should analyze the application logs using
two different methods.

Method 1:
Count the frequency of each Log Level using a traditional
if-else approach.

Method 2:
Count the frequency of each Log Level using Python's
dictionary get() method.

Instead of measuring execution time, compare the
efficiency of both methods by counting the number of
operations performed.

Assume the following:

• Method 1 performs one operation for processing each
  log record.

• Method 2 uses dictionary.get() and is considered an
  optimized approach.

• For evaluation purposes:

      If only one log record exists,
      Method 2 performs 1 operation.

      Otherwise,
      Method 2 performs 3 operations
      (one optimized operation for each valid log level:
      INFO, WARNING and ERROR).

Store all log records using a list.

The log analysis functions should use Python Type Hints.

After processing all log records:

• Display the frequency of each Log Level.

• Display the most frequently occurring Log Level.

• Display the number of operations performed by each
  method.

• Display the better performing method.

Requirements:
-------------
1. Store log records using a list.
2. Use Python Type Hints.
3. Implement Method 1 using if-else statements.
4. Implement Method 2 using dictionary get().
5. Count the number of operations.
6. Display the frequency of each Log Level.
7. Display the most frequent Log Level.
8. Display the better performing method.

Input Format:
-------------
First line contains the number of log records N.

Next N sets contain:

Log ID
Log Level
Module Name

Output Format:
--------------
Log Summary:

INFO : 2
WARNING : 1
ERROR : 3

Most Frequent Log Level : ERROR

Method 1 Operations : 6

Method 2 Operations : 3

Better Performing Method : Method 2

If N <= 0 display

Invalid Number of Log Records

If Log Level is not one of

INFO
WARNING
ERROR

display

Invalid Log Level

Sample Input:
-------------
6
L101
INFO
Login
L102
ERROR
Database
L103
WARNING
Memory
L104
INFO
Logout
L105
ERROR
Server
L106
ERROR
Network

Sample Output:
--------------
Log Summary:
INFO : 2
WARNING : 1
ERROR : 3

Most Frequent Log Level : ERROR

Method 1 Operations : 6

Method 2 Operations : 3

Better Performing Method : Method 2

Test Cases
----------

case=1
input=6
L101
INFO
Login
L102
ERROR
Database
L103
WARNING
Memory
L104
INFO
Logout
L105
ERROR
Server
L106
ERROR
Network
output=
Log Summary:
INFO : 2
WARNING : 1
ERROR : 3

Most Frequent Log Level : ERROR

Method 1 Operations : 6

Method 2 Operations : 3

Better Performing Method : Method 2


case=2
input=4
L201
WARNING
Disk
L202
WARNING
CPU
L203
INFO
Login
L204
WARNING
Memory

output=
Log Summary:
INFO : 1
WARNING : 3
ERROR : 0

Most Frequent Log Level : WARNING

Method 1 Operations : 4

Method 2 Operations : 3

Better Performing Method : Method 2


case=3
input=1
L301
INFO
Home
output=
Log Summary:

INFO : 1
WARNING : 0
ERROR : 0

Most Frequent Log Level : INFO

Method 1 Operations : 1

Method 2 Operations : 1

Better Performing Method : Both Methods


case=4
input=0
output=
Invalid Number of Log Records


case=5
input=2
L401
SUCCESS
Login
L402
INFO
Logout

output=
Invalid Log Level
"""
from typing import Literal, List, Union, Tuple

def get_input() -> List[Tuple[str, str, str]]:
    n = int(input())
    
    if n <= 0:
        raise ValueError("Invalid Number of Log Records")
    
    records = []
    log_level: Literal["INFO","WARNING","ERROR"]
    
    for _ in range(n):
        log_id = input()
        log_level = input()
        module_name = input()
        
        if log_level not in {"INFO","WARNING","ERROR"}:
            raise ValueError("Invalid Log Level")
            
        records.append((log_id, log_level, module_name))
    return records

class AnalyseLogs:
    def __init__(self, records: List[Tuple[str,str,str]]):
        self.records = records
    
    def method1(self) -> Union[List[int], int]:
        log_levels = ["INFO","WARNING","ERROR"]
        count_log = [0,0,0]
        op_count = 0
        for record in self.records:
            log_id, log_level, module_name = record
            if log_level == log_levels[0]:
                count_log[0] += 1
            elif log_level == log_levels[1]:
                count_log[1] += 1
            elif log_level == log_levels[2]:
                count_log[2] += 1
            op_count += 1
                
        return count_log,op_count
    
    def method2(self) -> Union[List[int],int]:
        if len(self.records) == 1:
            return [0,0,0], 1
        freq = {}
        op_count = 3
        for record in self.records:
            freq[record[1]] = freq.get(record[1],1)+1
        count_log = list(freq.values())
        
        return count_log, op_count
    
    def display(self):
        log_levels = ["INFO","WARNING","ERROR"]
        log_level1, count1 = self.method1()
        log_level2, count2 = self.method2()
        
        print("Log Summary:")
        for i in range(3):
            print(f"{log_levels[i]} : {log_level1[i]}")
            
        most_freq_log = max(zip(log_levels,log_level1), key= lambda x:x[-1])
        print(f"Most Frequent Log Level : {most_freq_log[0]}")
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
        records = get_input()
        al = AnalyseLogs(records)
        al.display()
    except ValueError as e:
        print(e)

main()