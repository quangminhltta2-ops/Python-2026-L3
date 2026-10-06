from domain import Student
import os
def ips():
    students = []
    if os.path.exists("student.txt"):
        with open("student.txt", "r") as file:
            for line in file:
                id, name, dob = line.strip().split(",")
                student = Student(
                    int(id),
                    name,
                    dob
                )
                students.append(student)
    else:
        N = int(input("Number of students: "))
        for i in range(N):
            id = int(input("ID: "))
            name = input("Name: ")
            dob = input("DoB: ")
            student = Student(
                id,
                name,
                dob
            )
            students.append(student)
        with open("student.txt", "w") as file:
            for student in students:
                file.write(
                    str(student.id) + "," +
                    student.name + "," +
                    student.dob + "\n"
                )
    return students