def print_triangle(number_of_star: int):
    for row in range(number_of_star):
        for column in range(row + 1):
            print("* ", end='')
        print()


print_triangle(5)


def print_triangle_reversed(number_of_star: int):
    for row in range(number_of_star, 0, -1):
        for column in range(0, row):
            print("* ", end='')
        print()


print_triangle_reversed(4)
