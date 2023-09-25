decimal_equivalent = 0
bit = 1
binary_integer = int(input("Enter a binary integer: "))
while binary_integer != 0:
    decimal_equivalent = decimal_equivalent + binary_integer % 10 * bit
    binaryInteger = binary_integer / 10
    bit *= 2
print("The decimal equivalent is: ", decimal_equivalent)
