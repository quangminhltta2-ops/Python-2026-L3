m = int(input("Enter m: "))
n = int(input("Enter n: "))
for i in range(m):
    if i == 0 or i == m - 1:
        print("* " * n)
    else:
        print("* " + "  " * (n - 2) + "*")