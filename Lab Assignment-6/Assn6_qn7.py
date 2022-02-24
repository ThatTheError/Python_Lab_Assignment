"""
7. Write a program that keeps student's name and his marks in a dictionary as key�value pairs. The program should store records of 10 students and display students
name and marks of five students in decreasing order of marks obtained.
"""

stud_details = {}
for i in range(10):
  nm=input("enter name of the student ")
  mark=int(input("enter mark obtained "))
  stud_details[nm] = mark

sorted(stud_details.items(),key=lambda x: x[1], reverse=True)
for i in stud_details:
  print(i, stud_details[i])