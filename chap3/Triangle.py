for row in range(10):
    for column in range(row + 1):
        print("*", end=' ')
    for column in range(10 - row):
        print(" ", end=' ')
    for column in range(0, 10 - row):
        print("*", end=' ')
    for column in range(0, 1 + row):
        print(" ", end=' ')
    for column in range(row + 1):
        print(" ", end=' ')
    for column in range(10 - row):
        print("*", end=' ')
    for column in range(10-row):
        print(" ", end=' ')
    for column in range(row + 1):
        print("*", end=' ')
    print()
