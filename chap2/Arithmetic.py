first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
answer = first_number + second_number + third_number
different = first_number - second_number - third_number
average = first_number + second_number + third_number / 3
product = first_number * second_number * third_number
print('The sum of:  ', first_number, 'and', second_number, 'is', answer)
print('The average of:  ', first_number, 'and', second_number, 'is', average)
print('The product is:  ', first_number, 'and', second_number, 'is', product)
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
