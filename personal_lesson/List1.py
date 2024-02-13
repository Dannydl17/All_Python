num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def largest_number(num):
    largest_number = num[0]
    for count in num:
        if count > largest_number:
            largest_number = count
    return largest_number


print(largest_number(num))


def reverse_number(number):
    temp = len(number)
    count = 0
    for counter in range(temp, 0, -1):
        temp = counter
        count += 1
        return temp


print(reverse_number(num))

# def even_number(num):
#     count = 0
#     for counter in num:
#         if counter % 2 == 0:
#             print(counter)
#             count = counter
#         #     new_index = 0
#         # for index in num:
#         #     if index % 2 == 0:
#         #         new_index = index
#         #         new_index += 1
#         # return new_index


# print(even_number(num))

# def odd_number(number):
#     count = 0
#     for counter in range(number):
#         if counter % 2 != 0:
#             count += 1
#             odd_number = [count]
#             new_index = 0
#             for index in range(number):
#                 if number[index] % 2 != 0:
#                     odd_number[new_index] = number[index]
#                     new_index += 1
#                 return odd_number
#
#
# def check_element(number):
#     counter = number[2]
#     for count in range(number):
#         if number[count] == counter:
#             return True
#         return False
#
#
# def running_total(number):
#     number_of_running_total = 0
#     for index in range(number):
#         number_of_running_total = number_of_running_total + number[index]
#     return number_of_running_total
#
# public static int sum(int[] element) {
#         int numberOfSum = 0;
#         for (int index = 0; index < element.length; index++) {
#             numberOfSum= numberOfSum+element[index];
#         }
#         return numberOfSum;
#     }
#
#
#     public static int sum1(int[] element) {
#         int numberOfSum = 0;
#         int index = 0;
#         while (index < element.length) {
#             numberOfSum= numberOfSum+element[index];
#             index++;
#         }
#         return numberOfSum;
#     }
# def isPalindrome():
#     reverse = ""
#     name = len(element.length)
#     for count in range()
#             reverse = reverse + name.charAt(count);
#
#         if (reverse.equals(name)) {
#             return true;
#         }
#         return false;
