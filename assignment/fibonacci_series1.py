def can_return_fibonacci_number(number):
    number_zero = 0
    nums = []
    sum_1 = 0
    number_one = 1

    for num in range(number):
        nums.append(number_zero)
        sum_1 = number_zero + number_one
        number_zero = number_one
        number_one = sum_1
    return nums


def can_find_the_largest_number(nums):
    largest_number = nums[0]
    for number in nums:
        if number > largest_number:
            largest_number = number
    return largest_number