# Use a for statement to print 10 random numbers.
# Repeat the above exercise but this time print 10 random numbers between 25 and 35, inclusive.

import random

for i in range(10):
    print("Random Number ", i+1, ": ", "\t", random.randint(25, 35))

input("Press enter to exit...")
