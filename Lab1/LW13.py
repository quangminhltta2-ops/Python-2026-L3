a = int(input("Enter a number: "))
b = 0
for i in range(2, a):
    if a % i == 0:
        b += 1
if b != 0:
    print(a, "is not a prime number")
else:
    print(a, "is a prime number")