def divide_or_square(number):
    numbers = number ** 0.50
    if number % 5 == 0:
        return numbers
    else:
        return numbers


answer = divide_or_square(701)
print(f'{answer:.2f}')
