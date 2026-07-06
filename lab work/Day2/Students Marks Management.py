students = {}

for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input(f"Enter marks of {name}: "))
    students[name] = marks

print("\nAll students and marks:")
for name, marks in students.items():
    print(name, "->", marks)

name = input("\nEnter the name of the student to add/update: ")
marks = int(input("Enter marks: "))
students[name] = marks

print("\nAfter adding/updating:")
for name, marks in students.items():
    print(name, "->", marks)

name = input("\nEnter the name of the student to delete: ")
if name in students:
    del students[name]
    print(name, "deleted successfully.")
else:
    print("Student not found.")

print("\nRemaining students:")
for name, marks in students.items():
    print(name, "->", marks)

highest_name = ""
highest_marks = -1
for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_name = name

print("\nStudent with highest marks:", highest_name, "->", highest_marks)