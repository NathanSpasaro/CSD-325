# Nathan Spasaro
# October 26, 2026
# CSD-325 Module 8 Assignment
# Purpose: Read, display, update, and save student information using JSON.

import json

def print_students(student_list):
    for student in student_list:
        print(F'{student["L_Name"]}, {student["F_Name"]} : ID = {student["Student_ID"]}, Email = {student["Email"]}')
with open("student.json", "r") as file:
    students = json.load(file)

print("Original Student List:")
print_students(students)

new_student = {
    "F_Name": "Nathan",
    "L_Name": "Spasaro",
    "Student_ID": 98765,
    "Email": "nspasaro@my365.bellevue.edu"
}

students.append(new_student)

print("\nUpdated Student List:")
print_students(students)

# Save the updated student list to the JSON file.
with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nstudent.json has been successfully updated.")