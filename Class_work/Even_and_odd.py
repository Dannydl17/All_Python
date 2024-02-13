numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def even_and_odd(numbers):
    odd_numbers = 0
    even_numbers = 0
    for num in numbers:
        if num % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
    return f'''
Odd numbers = {odd_numbers}
Even numbers = {even_numbers}
    '''




print(even_and_odd(numbers))