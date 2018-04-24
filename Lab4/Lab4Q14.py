# Write a function called mySqrt that will approximate the square root of a number,
# call it n, by using Newton’s algorithm.
# Newton’s approach is an iterative guessing algorithm
# where the initial guess is n/2 and each subsequent guess is computed using the formula:
# newguess = (1/2) * (oldguess + (n/oldguess)).


def newguessfunc(n,x):
    oldguess = x
    newguess = (1/2) * (oldguess + (n/oldguess))
    return newguess


numbertoRoot = int(input("Input a number to find the square root of: "))
guess = numbertoRoot/2

for i in range(1, 51):
    guess = newguessfunc(numbertoRoot, guess)
    print("Guess #", i, ": ", guess)

input("Press enter to continue...")
