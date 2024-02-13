total = 0
count = 0
while count < 10:
    student_score = int(input('Enter student score:  '))
    total += student_score
    count += 1
average = total / count
print("The average of the score is: ", average)
