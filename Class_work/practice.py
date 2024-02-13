def your_salary():
    global gross_salary
    name = input("Enter the teacher name:  ")
    number_of_period = int(input("Enter period:  "))
    monthly_rate = 20
    if 0 < number_of_period <= 100:
        gross_salary = number_of_period * monthly_rate
    if number_of_period > 100:
        gross_salary = 100 * monthly_rate + (number_of_period - 100) * 25
    return (f'Teacher: {name} \n'
            f'Period: {number_of_period} \n'
            f' Gross salary: {gross_salary}')


print(your_salary())
