nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def element_a_list(nums, target):
    counter = target
    for count in nums:
        if nums[count] == counter:
            return True
        else:
            return False


print(element_a_list(nums, 10))
