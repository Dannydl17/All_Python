limit = 20
for side1 in range(1, limit):
    for side2 in range(side1, limit):
        for side3 in range(side2, limit):
            if(side1**2) + (side2 ** 2) == (side3 ** 2):
                print(side1, side2, side3)
