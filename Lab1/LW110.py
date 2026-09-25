a = int(input("Enter a number: "))
b = []
for i in range(2, a):
    if a % i == 0:
        b.append(i)
print(*b, sep = ", ")