# Write a function that reverses its string argument.


def reversestring(x):
    x = str(x)
    y = len(x)
    z = ""
    for ch in range(y):
        z = x[ch] + z
    return z


stringinput = input("Enter a string to reverse: ")
stringinput = str(stringinput)
print(reversestring(stringinput))
