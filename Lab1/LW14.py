a = int(input("Enter a number: "))
b = []
c = 0
for i in range(1, a):
    if a % i == 0:
        b.append(i)
for i in range(len(b)):
    c += b[i]
if c == a:
    print(a, "is a perfect number")
else:
    print(a, "is not a perfect number")