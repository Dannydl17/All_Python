def list_number():
    return list(range(1, 21))


def list_number2(list1):
    res = []
    for number in list1:
        if number % 2 == 1:
            res.append(number)
    return res
    # return [i for i in list1 if i % 2 !=0]##### list comprehension


def list_number3(list1):
    return [i * 2 for i in list1 if i % 2 == 1]


def list_number4(list1):
    result = [i * 2 for i in list1 if i % 2 == 1]
    result[4:8] = [0] * len(list1[4:8])
    return result


def list_number5(list1, list2):
    return [x + y for x, y in zip(list1, list2)]
