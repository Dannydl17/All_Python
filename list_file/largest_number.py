number = [15, 20, 25, 20, 10, 5]


def largest_number(number):
    largest_number = number[0]
    for count in number:
        if count > largest_number:
            largest_number = count
    return largest_number


print(largest_number(number))
