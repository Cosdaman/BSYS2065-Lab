# Write a function called remove_dups that takes a string and creates a new string by only adding
# those characters that are not already present.
# In other words, there will never be a duplicate letter added to the new string.


def remove_dups(x):
    xlen = len(x)
    newstring = ""
    for i in range(xlen):
        if x[i] not in newstring:
            newstring = newstring + x[i]
        else:
            pass
    return newstring


stringinput = str(input("Please input a string: "))
print(remove_dups(stringinput))
