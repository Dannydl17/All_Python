numbers = int(input("Enter a number: "))
largest_number = numbers
second_largest_number = 0

for counter in range(10):
    numbers = int(input("Enter a number: "))

    if numbers > largest_number:
        second_largest_number = largest_number
        largest_number = numbers
    elif numbers > second_largest_number:
        second_largest_number = numbers
print(f'''
The largest_number is:   {largest_number}
The second_largest_number is: {second_largest_number}
 ''')
