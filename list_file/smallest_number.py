number = [15, 20, 25, 20, 10, 5]


def smallest_number(number):
    smallest_number = number[0]
    for count in number:
        if count < smallest_number:
            smallest_number = count
    return smallest_number


print(smallest_number(number))

