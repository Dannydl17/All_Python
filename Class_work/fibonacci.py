first_number = 1
count = 0
number = first_number + count
while count < 50:
    print(count, end='')
    count = first_number
    first_number = number
    number = count + first_number
    print(first_number, end=' ')
