def even(l):
    a = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            a.append(l[i])
    return a
b = int(input("Length: "))
c = []
for i in range(b):
    d = int(input("Value: "))
    c.append(d)
print(even(c))