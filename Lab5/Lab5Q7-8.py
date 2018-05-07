# Now write the function is_odd(n) that returns True when n is odd and False otherwise.


def is_odd(n):
    if n % 2 == 0:
        return False
    else:
        return True


x = int(input("Input a number to see if it is odd: "))
print(is_odd(x))
