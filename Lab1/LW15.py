a = input("What is your favorite color? ")
b = ["Green", "Blue", "Red", "Yellow"]
c = 0
for i in range(len(b)):
    if a == b[i]:
        print("Your colod is at index", i, "in my list")
        c += 1
        break
if c == 0:
    print("Sorry, I could not find your color")