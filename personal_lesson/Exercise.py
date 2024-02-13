first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
third_number = int(input('Enter the third number: '))
highest_number = first_number
if second_number > highest_number:
    highest_number = second_number
if third_number > highest_number:
    highest_number = third_number
print("The highest number is: ", highest_number)