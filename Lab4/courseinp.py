from domain import Course
def ipc(students):
    courses = []
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
    return courses