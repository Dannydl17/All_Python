principal = int(input('Enter the principal:  '))
rate = int(input('Enter an annual rate:  '))
number_of_year = int(input('Enter the number of year:  '))

number_of_rate = rate / 100
for numbers in range(1, number_of_year):
    amount = principal * (1 + number_of_rate) ** numbers
    print(amount)
