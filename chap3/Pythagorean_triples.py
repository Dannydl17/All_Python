limit = 500
side1 = int(input("Pythagorean Triples (side1, side2, hypotenuse): "))
for side1 in range(1, limit):
    for side2 in range(1, limit):
        for hypotenuse in range(limit):
            print(side1 + ", " + side2 + ", " + hypotenuse)
