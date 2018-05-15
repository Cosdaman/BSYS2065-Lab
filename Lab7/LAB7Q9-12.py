# Write a function that removes all occurrences of a string from another string.
import string

def removestring(stringthing, stringremovething):
    x = stringthing.replace(stringremovething, "")
    return x


stringitem = str(input("Enter a string: "))
lettertoremove = str(input("Enter a smaller string  to remove from the string: "))
print(removestring(stringitem, lettertoremove))
