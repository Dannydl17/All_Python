multiples = 6
count = 1
while count < 3000:
    result = multiples * count
    count *= 6
    if result < 3000:
        print(result, end=' ')
