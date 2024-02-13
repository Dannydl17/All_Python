def can_return_equal_string(first_string, second_string):
    for i in range(len(first_string)):
        for j in range(len(second_string)):
            if i == j:
                return True
    return False
