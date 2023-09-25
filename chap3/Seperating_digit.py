number = int(input('Enter the five number: '))
for numbers in range(number):
    number1 = numbers // 10000
    number2 = numbers % 10000 // 1000
    number3 = numbers % 1000 // 100
    number4 = numbers % 100 // 10
    number5 = numbers % 10
print('number5\tnumber4\tnumber3\tnumber2\tnumber1', number1, number2, number3, number4, number5)
