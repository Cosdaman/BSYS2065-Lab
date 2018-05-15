# Write a function that removes all occurrences of a given letter from a string.


def removeletter(stringthing,letterthing):
    x = int(len(stringthing))
    newstring = ""
    for i in range(x):
        if letterthing != stringthing[i]:
            newstring = newstring + stringthing[i]
        else:
            pass
    return newstring


stringitem = str(input("Enter a string: "))
lettertoremove = str(input("Enter a letter to remove from the string: "))
print(removeletter(stringitem, lettertoremove))
