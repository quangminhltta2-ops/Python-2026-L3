a = []
for i in range(7):
    a.append(i)
print(*a, sep = ", ")
a.clear()
for i in range(1, 11, 3):
    a.append(i)
print(*a, sep = ", ")
a.clear()
for i in range(5, 0, -1):
    a.append(i)
print(*a, sep = ", ")
a.clear()
for i in range(6, -3, -2):
    a.append(i)
print(*a, sep = ", ")
a.clear()