<<<<<<< HEAD
number = [15, 20, 25, 20, 10, 5]


# def largest_number(number):
#     largest_number = number[0]
#     for count in number:
#         if count > largest_number:
#             largest_number = count
#     return largest_number
#
#
# print(largest_number(number))


# def smallest_number(number):
#     smallest_number = number[0]
#     for count in number:
#         if count < smallest_number:
#             smallest_number = count
#     return smallest_number
#
#
# print(smallest_number(number))


# def sum_of_list(number):
#     list_length = len(number)
#     sum_of_elements = 0
#     for count in range(list_length):
#         sum_of_elements = sum_of_elements + number[count]
#     return sum_of_elements
#
#
# print(sum_of_list(number))


# def multiply_list(number):
#     list_length = len(number)
#     print(number)
#     multiples_of_elements = 1
#     for count in range(list_length):
#         multiples_of_elements = multiples_of_elements * number[count]
#     return multiples_of_elements
#
#
# print(multiply_list(number))


def duplicate_list(number):
    result = []
    for count in number:
        if count not in result:
            result.append(count)
    return result


print(duplicate_list(number))
=======
number = [15, 20, 25, 20, 10, 5]


# def largest_number(number):
#     largest_number = number[0]
#     for count in number:
#         if count > largest_number:
#             largest_number = count
#     return largest_number
#
#
# print(largest_number(number))


# def smallest_number(number):
#     smallest_number = number[0]
#     for count in number:
#         if count < smallest_number:
#             smallest_number = count
#     return smallest_number
#
#
# print(smallest_number(number))


# def sum_of_list(number):
#     list_length = len(number)
#     sum_of_elements = 0
#     for count in range(list_length):
#         sum_of_elements = sum_of_elements + number[count]
#     return sum_of_elements
#
#
# print(sum_of_list(number))


# def multiply_list(number):
#     list_length = len(number)
#     print(number)
#     multiples_of_elements = 1
#     for count in range(list_length):
#         multiples_of_elements = multiples_of_elements * number[count]
#     return multiples_of_elements
#
#
# print(multiply_list(number))


def duplicate_list(number):
    result = []
    for count in number:
        if count not in result:
            result.append(count)
    return result


print(duplicate_list(number))
>>>>>>> 4cae69ed4c208ef345a83b1bc2d387f34866cd69
