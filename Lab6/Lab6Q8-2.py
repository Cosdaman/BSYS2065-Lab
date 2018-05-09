# Write a function print_triangular_numbers(n) that prints out the first n triangular numbers.
# A call to print_triangular_numbers(5) would produce the following output:
# 1       1
# 2       3
# 3       6
# 4       10
# 5       15


def print_triangular_numbers(n):
    number = int(0)
    for i in range(1, n+1):
        number = number + i
        print(i, "\t", number)


x = int(input("How many triangular numbers do you want to see? Enter here: "))

print_triangular_numbers(x)

