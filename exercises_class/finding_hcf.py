def find_hcf(numbers):
    number1, number2 = numbers[0], numbers[1]
    hcf = find_hcf(number1, number2)

    if len(numbers) > 2:
        for index in numbers[2:]:
            hcf = find_hcf(hcf, index)

    return hcf


def find_hcf(a, b):
    if b == 0:
        return a
    else:
        return find_hcf(b, a % b)


nums = 8, 16, 12
print(find_hcf(nums))
