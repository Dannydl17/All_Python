first_number = int(input("Enter first number: "))
square_a = first_number * first_number
cube_a = first_number * first_number * first_number

second_number = int(input("Enter second number: "))
square_b = second_number * second_number
cube_b = second_number * second_number * second_number

third_number = int(input("Enter third number: "))
square_c = third_number * third_number
cube_c = third_number * third_number * third_number

fourth_number = int(input("Enter fourth number: "))
square_d = fourth_number * fourth_number
cube_d = fourth_number * fourth_number * fourth_number

fifth_number = int(input("Enter fifth number: "))
square_e = fifth_number * fifth_number
cube_e = fifth_number * fifth_number * fifth_number

sixth_number = int(input("Enter sixth number: "))
square_f = sixth_number * sixth_number
cube_f = sixth_number * sixth_number * sixth_number

print(" number square cube")
print('{0:4d} {1:5d} {2:6d}'.format(first_number, square_a, cube_a))
print('{0:4d} {1:5d} {2:6d}'.format(second_number, square_b, cube_b))
print('{0:4d} {1:5d} {2:6d}'.format(third_number, square_c, cube_c))
print('{0:4d} {1:5d} {2:6d}'.format(fourth_number, square_d, cube_d))
print('{0:4d} {1:5d} {2:6d}'.format(fifth_number, square_e, cube_e))
print('{0:4d} {1:5d} {2:6d}'.format(sixth_number, square_f, cube_f))

