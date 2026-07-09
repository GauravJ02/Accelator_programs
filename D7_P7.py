"""
Problem Title: Smart Student Marks Matrix Analyzer

Problem Statement:

A university stores the marks of students in multiple
subjects using a NumPy matrix.

Each row represents one student.

Each column represents one subject.

The examination department wants to analyze the
performance of the class.

The program should calculate:

• Student-wise Total Marks
• Student-wise Average Marks
• Subject-wise Average Marks
• Overall Class Average
• Top Scorer (Highest Total Marks)

The marks should be stored in a NumPy 2D Array.

The marks matrix should be created using reshape().

The calculations should use NumPy vectorized functions
without using nested loops.

Requirements:
-------------
1. Store marks in a NumPy array.
2. Convert the array into a matrix using reshape().
3. Calculate student-wise total.
4. Calculate student-wise average.
5. Calculate subject-wise average.
6. Calculate overall class average.
7. Display the Top Scorer.

Input Format:
-------------
First line contains the number of students N.

Second line contains the number of subjects M.

Next N × M lines contain the marks.

Output Format:
--------------
Student Totals:
Student 1 : <total>
Student 2 : <total>
...

Student Averages:
Student 1 : <average>
Student 2 : <average>
...

Subject Averages:
Subject 1 : <average>
Subject 2 : <average>
...

Overall Class Average : <average>

Top Scorer : Student <number>

If N <= 0 display

Invalid Number of Students

If M <= 0 display

Invalid Number of Subjects

If any mark is less than 0 or greater than 100 display

Invalid Marks

Sample Input:
-------------
3
3
80
70
90
60
75
85
95
90
80

Sample Output:
--------------
Student Totals:
Student 1 : 240
Student 2 : 220
Student 3 : 265

Student Averages:
Student 1 : 80.0
Student 2 : 73.33
Student 3 : 88.33

Subject Averages:
Subject 1 : 78.33
Subject 2 : 78.33
Subject 3 : 85.0

Overall Class Average : 80.56

Top Scorer : Student 3

Test Cases
----------

case=1
input=
3
3
80
70
90
60
75
85
95
90
80

output=
Student Totals:
Student 1 : 240
Student 2 : 220
Student 3 : 265

Student Averages:
Student 1 : 80.0
Student 2 : 73.33
Student 3 : 88.33

Subject Averages:
Subject 1 : 78.33
Subject 2 : 78.33
Subject 3 : 85.0

Overall Class Average : 80.56
Top Scorer : Student 3

case=2
input=
2
2
90
95
80
85
output=
Student Totals:
Student 1 : 185
Student 2 : 165

Student Averages:
Student 1 : 92.5
Student 2 : 82.5

Subject Averages:
Subject 1 : 85.0
Subject 2 : 90.0

Overall Class Average : 87.5

Top Scorer : Student 1


case=3
input=
1
3
75
80
85
output=
Student Totals:
Student 1 : 240

Student Averages:
Student 1 : 80.0

Subject Averages:
Subject 1 : 75.0
Subject 2 : 80.0
Subject 3 : 85.0

Overall Class Average : 80.0

Top Scorer : Student 1

case=4
input=
0
3
output=
Invalid Number of Students


case=5
input=
2
2
80
105
70
60
output=
Invalid Marks
"""
import numpy as np

def get_input():
    n = int(input())
    m = int(input())
    if n <= 0:
        raise ValueError("Invalid Number of Students")
    elif m <= 0:
        raise ValueError("Invalid Number of Subjects")
        
    students = []
    check_mark = True
    
    for i in range(n):
        subject = []
        for j in range(m):
            mark = int(input())
            if not 0 <= mark <= 100:
                check_mark = False
            subject.append(mark)
        students.append(subject)
            
    if not check_mark:
        raise ValueError("Invalid Marks")
    
    students = np.array(students).reshape(n,m)
    return students
    
class MarksAnalyser:
    def __init__(self, marks):
        self.marks = marks
    
    def student_total(self):
        total = self.marks.sum(axis=1)
        return total
    
    def student_avg(self):
        avg = self.marks.mean(axis=1)
        return avg
    
    def subject_avg(self):
        total = self.marks.mean(axis=0)
        return total
        
    def class_avg(self):
        return round(self.marks.mean(),2)
        
    def topper(self):
        return self.student_total().argmax()+1
        
    def display(self):
        print("Student Totals:")
        for i, total in enumerate(self.student_total()):
            print(f"Student {i+1} : {total}")
        print()
        
        print("Student Averages:")
        for i, avg in enumerate(self.student_avg()):
            print(f"Student {i+1} : {round(avg,2)}")
        print()
        
        print("Subject Averages:")
        for i, avg in enumerate(self.subject_avg()):
            print(f"Subject {i+1} : {round(avg,2)}")
        print()
        print(f"Overall Class Average : {self.class_avg()}")
        print()
        print(f"Top Scorer : Student {self.topper()}")

def main():
    try:
        marks = get_input()
        ma = MarksAnalyser(marks)
        ma.display()
    except ValueError as e:
        print(e)

main()