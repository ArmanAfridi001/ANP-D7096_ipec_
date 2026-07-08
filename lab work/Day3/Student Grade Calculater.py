def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"


def find_max(numbers):
    return max(numbers)


def find_min(numbers):
    return min(numbers)


def find_average(numbers):
    return sum(numbers) / len(numbers)


def student_grade_calculator():
    print("Student Grade Calculator")
    print("-" * 28)

    student_marks = []

    for student in range(1, 6):
        while True:
            try:
                marks = int(input(f"Enter marks for student {student}: "))
                if 0 <= marks <= 100:
                    student_marks.append(marks)
                    break
                else:
                    print("Marks should be between 0 and 100.")
            except ValueError:
                print("Please enter a valid integer.")

    for marks in student_marks:
        grade = calculate_grade(marks)
        print(f"Marks: {marks} -> Grade: {grade}")


def list_analysis():
    print("\nList Analysis using Functions")
    print("-" * 32)

    numbers = []

    while len(numbers) < 10:
        try:
            value = int(input(f"Enter integer {len(numbers) + 1}: "))
            numbers.append(value)
        except ValueError:
            print("Please enter a valid integer.")

    print("Entered list:", numbers)
    print("Maximum:", find_max(numbers))
    print("Minimum:", find_min(numbers))
    print("Average:", find_average(numbers))


if __name__ == "__main__":
    student_grade_calculator()
    list_analysis()