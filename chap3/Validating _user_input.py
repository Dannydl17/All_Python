passes = 0
failures = 0
studentCounter = 1
result = 0

while studentCounter <= 10:
    result = int(input("Enter result (1 = pass, 2 = fail): "))
    if result == 1:
        passes = passes + 1
        studentCounter = studentCounter + 1
    elif result == 2:
        failures = failures + 1
        studentCounter = studentCounter + 1
    else:
        print("Invalid Input")
print(f'''
Passed: {passes} 
Failed: {failures}
''')