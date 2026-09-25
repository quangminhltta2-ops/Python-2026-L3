def remove_dollar_sign(s):
    s = s.replace("$", "")
    return s
a = input("Enter string: ")
print(remove_dollar_sign(a))