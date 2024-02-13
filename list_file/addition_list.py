number = [15, 20, 25, 20, 10, 5]


def sum_of_list(number):
    list_length = len(number)
    sum_of_elements = 0
    for count in range(list_length):
        sum_of_elements = sum_of_elements + number[count]
    return sum_of_elements


print(sum_of_list(number))
