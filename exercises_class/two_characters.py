def can_pick_single_string(words):
    result = []
    count = 0
    for nums in words:
        n = nums.split('.')
        if ',' == n:
            print(n)
            count += 1

