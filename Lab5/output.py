import numpy as np
def ps(students):
    print("\nStudents")
    for student in students:
        print(
            student.id,
            student.name,
            student.dob
        )     
def pc(courses):
    print("\nCourses")
    for course in courses:
        print(
            course.id,
            course.name
        )
def pcm(courses, students):
    course_id = int(input("\nEnter course ID: "))
    for course in courses:
        if course.id == course_id:
            print("\nMarks for", course.name)
            for student in students:
                mark = course.marks[student.id]
                print(student.name, ":", mark)
def sgpa(students, courses):
    for student in students:
        marks = []
        credits = []
        for course in courses:
            marks.append(course.marks[student.id])
            credits.append(course.credit)
        marks = np.array(marks)
        credits = np.array(credits)
        student.GPA = np.sum(marks * credits) / np.sum(credits)
    students.sort(
        key=lambda student: student.GPA,
        reverse=True
    )
    print("\nGPA:")
    for student in students:
        print(
            student.id,
            student.name,
            "GPA:",
            student.GPA
        )
