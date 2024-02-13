def score():
    total = 0
    numbers = []
    for number in range(10):
        num = int(input("Enter score: "))
        total += num
        numbers.append(num)
    print(numbers)

    average = total / 10
    print(average)


print(score())
