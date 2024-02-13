# num1 = []


def can_return_largest(num):
    # nums = int(num)
    result = int(max([i for i in num if int(i) % 2 == 1]))
    return result
    # while nums > 0:
    #     total = nums % 10
    #     num1.append(total)
    #     nums //= 10
    #     largest = num1[0]
    # for i in num1:
    #     if i > largest:
    #         largest = i
    # return largest
