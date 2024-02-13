def fibonacci(number: int):
    first_number = 0  # The x is the start
    count = 1
    total = first_number + count
    while first_number < number:
        print(first_number, end=' ')
        count = first_number
        first_number = total
        total = count + first_number


fibonacci(200)
