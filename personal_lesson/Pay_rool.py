name = input("Enter employee's name: ")
number_Of_hour = float(input('Enter number of hours worked in a week: '))
hourly_Rate = float(input('Enter hourly rate: '))
month = input('Enter month of the year: ')
federal_Rate = int(input('Enter federal tax withholding rate:  '))
state_Rate = int(input('Enter number of hours worked in a week:  '))

gross_Pay = hourly_Rate * number_Of_hour
federal_Withholding = gross_Pay * 20 / 100
state_Withholding = gross_Pay * 9 / 100
total_Deduction = federal_Withholding + state_Withholding
net_Pay = gross_Pay - total_Deduction
print(f'''
Divine Mercy Payroll statement for the month of April
Employee Name: {name}
Hour Worked: {number_Of_hour}
Month: {month}
Pay Rate:  $ {hourly_Rate}
Gross Pay: $ {gross_Pay}
Deductions:
Federal Withholding: $ {federal_Withholding}
State Withholding: $ {state_Withholding}
Total Deduction: $ {total_Deduction}
Net Pay: $  {net_Pay}
'''
)
