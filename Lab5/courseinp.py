import os
from domain import Course
def ipc(students):
    courses = []
    if os.path.exists("course.txt"):
        with open("course.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                id = int(data[0])
                name = data[1]
                credit = int(data[2])
                course = Course(id, name, credit)
                for i in range(len(students)):
                    student_id = students[i].id
                    mark = float(data[3 + i])
                    course.marks[student_id] = mark
                courses.append(course)
    else:
        Nc = int(input("\nNumber of courses: "))
        for i in range(Nc):
            print("\nCourse", i + 1)
            id = int(input("Course ID: "))
            name = input("Course name: ")
            credit = int(input("Credit: "))
            course = Course(id, name, credit)
            courses.append(course)
        for course in courses:
            print("\nCourse:", course.name)
            for student in students:
                mark = float(input(
                    "Mark for " + student.name + ": "
                ))
                course.marks[student.id] = mark
        with open("course.txt", "w") as file:
            for course in courses:
                file.write(
                    str(course.id) + "," +
                    course.name + "," +
                    str(course.credit)
                )
                for student in students:
                    file.write(
                        "," +
                        str(course.marks[student.id])
                    )
                file.write("\n")
    return courses