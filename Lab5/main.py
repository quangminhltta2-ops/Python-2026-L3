import os
import pickle
import numpy as np

from stdinput import ips
from courseinp import ipc
from output import ps, pc, pcm, sgpa
if os.path.exists("student.dat"):
    with open("student.dat", "rb") as file:
        students = pickle.load(file)
        courses = pickle.load(file)
else:
    students = ips()
    courses = ipc(students)
    with open("student.dat", "wb") as file:
        pickle.dump(students, file)
        pickle.dump(courses, file)
sgpa(students, courses)
ps(students)
pc(courses)
pcm(courses, students)