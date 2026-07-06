employees = {
    101: {"name": "Ali", "department": "IT", "salary": 50000},
    102: {"name": "Sara", "department": "HR", "salary": 45000},
    103: {"name": "Hassan", "department": "Finance", "salary": 60000},
}

print("All employee details:")
for emp_id, details in employees.items():
    print("Employee ID:", emp_id)
    print("Name:", details["name"])
    print("Department:", details["department"])
    print("Salary:", details["salary"])
    print()

search_id = int(input("Enter Employee ID to search: "))
if search_id in employees:
    details = employees[search_id]
    print("\nEmployee found:")
    print("Name:", details["name"])
    print("Department:", details["department"])
    print("Salary:", details["salary"])
else:
    print("Employee not found.")

for emp_id in employees:
    employees[emp_id]["salary"] = employees[emp_id]["salary"] * 1.10

print("\nSalary increased by 10%:")
for emp_id, details in employees.items():
    print("Employee ID:", emp_id, "Salary:", details["salary"])

dept = input("\nEnter department to display employees: ")
print("\nEmployees in", dept, ":")
for emp_id, details in employees.items():
    if details["department"] == dept:
        print("Employee ID:", emp_id, "Name:", details["name"])