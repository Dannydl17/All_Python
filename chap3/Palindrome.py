originalNumber = int(input('Enter five digits numbers: '))
numbers = originalNumber
reversedNumber = 0

while numbers != 0:
    remainder = numbers % 10
    reversedNumber = reversedNumber * 10 + remainder
    numbers = numbers // 10
if originalNumber == reversedNumber:
    print(originalNumber, "Number is a Palindrome number")
else:
    print(originalNumber, "Number is not a Palindrome")
