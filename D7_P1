"""
A software company processes the monthly payroll of its employees.

Each employee record contains:

Employee ID
Employee Name
Department
Basic Salary
Bonus

The bonus may or may not be available for every employee.

The payroll system should calculate the Net Salary using the following formula:

Net Salary = Basic Salary + Bonus

If the bonus is not available, it should be treated as 0.

Store all employee records using a dictionary where: Employee ID → (Employee Name, Department, Basic Salary, Bonus)

After processing all employees, display the employee payroll sorted in descending order of Net Salary.

The payroll calculation function should use Python Type Hints.

The bonus parameter should use Optional.

The salary values should use Union[int, float].

Requirements:
---------------
Store employee records using a dictionary.
Create a payroll calculation function using Type Hints.
Use Optional for Bonus.
Use Union[int, float] for salary values.
Sort employees using a lambda expression.
Display Net Salary for every employee.

Input Format
-------------
The first line contains the number of employees N.
The next N sets contain:
Employee ID
Employee Name
Department
Basic Salary
Bonus

If bonus is not available, the input will be:None

Output Format:
---------------
Employee Payroll:

E101 -> Ravi -> Development -> 65000
E103 -> Rahul -> Testing -> 56000
E102 -> Priya -> HR -> 50000


sample input:
3
E101
Ravi
Development
60000
5000
E102
Priya
HR
50000
None
E103
Rahul
Testing
55000
1000

Sample Output:
Employee Payroll:
E101 -> Ravi -> Development -> 65000
E103 -> Rahul -> Testing -> 56000
E102 -> Priya -> HR -> 50000

Test Cases
-----------
case=1
input=3
E101
Ravi
Development
60000
5000
E102
Priya
HR
50000
None
E103
Rahul
Testing
55000
1000
output=
Employee Payroll:
E101 -> Ravi -> Development -> 65000
E103 -> Rahul -> Testing -> 56000
E102 -> Priya -> HR -> 50000

case=2
input=2
E201
Anu
Testing
40000
None
E202
Kiran
Development
45000
5000
output=
Employee Payroll:
E202 -> Kiran -> Development -> 50000
E201 -> Anu -> Testing -> 40000

case=3
input=1
E301
Ajay
HR
35000
2500
output=
Employee Payroll:
E301 -> Ajay -> HR -> 37500


case=4
input=1
E401
Ramesh
Testing
-5000
1000
output=
Invalid Basic Salary


case=5
input=1
E501
Pooja
Development
45000
-500
output=
Invalid Bonus

case=6
input=0
output=
Invalid Number of Employees
"""

from typing import Optional
from typing import Union


def get_input():
    n = int(input())
    if n <= 0:
        raise ValueError("Invalid Number of Employees")
        
    employee_record = {}
    basic_salary: Union[int,float]

    for _ in range(n):
        emp_id = input()
        emp_name = input()
        dep = input()
        basic_salary = int(input())
        bonus = input()
        if basic_salary <= 0:
            raise ValueError("Invalid Basic Salary")
        if not bonus.isdigit() and bonus != "None":
            raise ValueError("Invalid Bonus")
                
        employee_record[emp_id] = (emp_name, dep, basic_salary, bonus)
    return employee_record


class PayrollSystem:
    def __init__(self,employee_record):
        self.employee_record = employee_record
    
    def calculate_payroll(self,salary: Union[int,float],bonus: Optional[int]) -> Union[int,float]:
        if bonus == "None":
            bonus = 0
        NetSalary = salary + int(bonus)
        return NetSalary
        
    def process_data(self):
        processed_data = []
        for emp_id, data in self.employee_record.items():
            emp_name, dep, basic_sal, bonus = data
            net_salary = self.calculate_payroll(basic_sal, bonus)
            processed_data.append([emp_id, emp_name, dep, net_salary])
        return processed_data
        
    def display(self):
        data = self.process_data()
        print("Employee Payroll:")
        sorted_data = sorted(data, key=lambda x:-x[-1])
        for emp_id, emp_name, dep, net_salary in sorted_data:
            print(f"{emp_id} -> {emp_name} -> {dep} -> {net_salary}")

def main():
    try:
        data = get_input()
        ps = PayrollSystem(data)
        ps.display()
    except ValueError as e:
        print(e)

main()