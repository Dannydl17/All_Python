first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
answer = first_number + second_number + third_number
different = first_number - second_number - third_number
average = first_number + second_number + third_number / 3
product = first_number * second_number * third_number
smallest_number = second_number
if first_number < smallest_number:
    smallest_number = first_number
if third_number < second_number:
    smallest_number = third_number
largest_number = first_number
if second_number > largest_number:
    largest_number = second_number
if third_number > largest_number:
    largest_number = third_number
print(f'''
The sum of:  {answer}
The average of: {average}
The product is: {product}
smallest_number is {smallest_number}
largest_number is {largest_number}
''')
