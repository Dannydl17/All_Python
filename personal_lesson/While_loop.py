total = 0
count = 0
student_score = int(input('Enter student score or press - 10 to quit:  '))
while student_score != - 10:
    total += student_score
    count += 1
    student_score = int(input('Enter student score or press - 10 to quit:  '))
average = total / count
print(f"The average of the score is:  {average:.2f}")
