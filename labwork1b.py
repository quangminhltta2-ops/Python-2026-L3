N = int(input("Number of students: "))
students = []
courses = []
for i in range(N):
    id = int(input("ID: "))
    name = input("Name: ")
    dob = input("DoB: ")
    s = {
        "id": id,
        "name": name,
        "DoB": dob
    }
    students.append(s)
print(students)
Nc = int(input("\nNumber of courses: "))
for i in range(N):
    print("\nCourse", i + 1)
    id = int(input("Course ID: "))
    name = input("Course name: ")
    c = {
        "id": id,
        "name": name,
        "marks": {}
    }
    courses.append(c)
for course in courses:
        print("\nCourse:", course["name"])
        for student in students:
            mark = float(input(
                "Mark for " + student["name"] + ": "))
            course["marks"][student["id"]] = mark
print("\nStudents ")
for student in students:
    print(student["id"], student["name"], student["dob"])
print("\nCourses")
for course in courses:
    print(
        course["id"],
        course["name"]
    )
course_id = int(input("\nEnter course ID: "))
for course in courses:
    if course["id"] == course_id:
        print("\n--- Marks for", course["name"], "---")
        for student in students:
             mark = course["marks"][student["id"]]
             print(
                 student["name"],
                ":",
                mark
            )
