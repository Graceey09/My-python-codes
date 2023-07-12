def print_triangle(number_of_rows):
    for i in range(number_of_rows + 1):
        print("*" * i, end=' ')
        print()


# row = 10
print_triangle(10)
print()


def print_triangle(number_of_rows):
    for b in range(number_of_rows, 0, -1):
        print(" " * (number_of_rows - b) + "*" * b)


row = 10
print_triangle(row)
print()


def print_triangle(number_of_rows):
    for b in range(number_of_rows, 0, -1):
        print("*" * b)


row = 10
print_triangle(row)
print()


def print_triangle(number_of_rows):
    for b in range(number_of_rows + 1):
        print(" " * (number_of_rows - b) + "*" * b)


row = 10
print_triangle(row)
print()


def print_circle(lines):
    for i in range(lines + 1):
        for j in range(i):
            print("*", end=' ')