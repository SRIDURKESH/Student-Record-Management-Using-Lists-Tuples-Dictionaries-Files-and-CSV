# Student Record Management with List, Tuple, Dictionary and CSV

import csv

# Get course details from user
course_name = input("Enter Course Name: ")
credits = int(input("Enter Course Credits: "))

# Tuple example
course = (course_name, credits)
print("Course Tuple:", course)

# Get student details
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    mark = float(input("Enter Mark: "))

    student = {
        "RollNo": roll,
        "Name": name,
        "Department": dept,
        "Mark": mark
    }

    students.append(student)

# Write text file
with open("students.txt", "w") as file:
    for student in students:
        file.write(str(student) + "\n")

print("\nStudent records saved to text file.")

# Write CSV file
with open("students.csv", "w", newline="") as file:
    fields = ["RollNo", "Name", "Department", "Mark"]

    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)

print("Student records saved to CSV file.")

# Read CSV file
print("\n--- Records from CSV ---")

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["RollNo"], row["Name"],
              row["Department"], row["Mark"])