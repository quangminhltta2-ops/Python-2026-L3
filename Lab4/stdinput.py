from domain import Student
def ips():
    students = []
    N = int(input("Number of students: "))
    for i in range(N):
        id = int(input("ID: "))
        name = input("Name: ")
        dob = input("DoB: ")
        student = Student(id, name, dob)
        students.append(student)
    return students