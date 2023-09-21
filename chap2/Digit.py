number = int(input('Enter the five digit number: '))
print(number)
number1 = number // 10000
number2 = number % 10000 // 1000
number3 = number % 1000 // 100
number4 = number % 100 // 10
number5 = number % 10
print('number5\tnumber4\tnumber3\tnumber2\tnumber1: ', number1, number2, number3, number4, number5)
