number = int(input("Enter an integer: "))

factorial = 1

for counter in range(number):
    factorial = factorial * (number - counter)
print("Factorial is: ", factorial)
