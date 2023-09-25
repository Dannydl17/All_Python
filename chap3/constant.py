number = int(input("Enter a number: "))
odd = 1
pi = 0.0
for numbers in range(1, number):
    current_term = 0.0
    if numbers % 2 == 0:
        currentTerm = float(- 4 / odd)
    else:
        currentTerm = float(4 / odd)
        odd = odd + 2
        pi = pi + currentTerm
        print(pi)
