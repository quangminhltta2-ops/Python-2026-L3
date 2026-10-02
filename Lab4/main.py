import numpy as np
from stdinput import ips
from courseinp import ipc
from output import (ps, pc, pcm, sgpa)
students = ips()
courses = ipc(students)
sgpa(students, courses)
ps(students)
pc(courses)
pcm(courses, students)