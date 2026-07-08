def search_student(student_dict, roll_no):
    if roll_no in student_dict:
        return student_dict[roll_no]
    else:
        return "Student Not Found"


students = {
    101: "Ali",
    102: "Sara",
    103: "Ahmed",
    104: "Nadia",
    105: "Omar"
}

roll_no = int(input("Enter roll number: "))
print(search_student(students, roll_no))