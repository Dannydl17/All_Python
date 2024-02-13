with open("demo.txt", mode='w') as file:
    file.write("Dan is the bravest!\n")
    file.write("Dan is also smart\n")
    file.write("Dan is also intelligent\n")


with open("demo.txt", mode='a') as file:
    file.write("Dan is the bravest!\n")
    file.write("Dan is also smart\n")
    file.write("Dan is also intelligent")

with open("demo.txt", mode='r') as file:
    print(f'{"First":<10}{"Second":<10}{"Third":<10}{"Fourth":>10}')
    for each in file:
        first, second, third, fourth, *others = each.split()
        print(f'{first:<10}{second:<10}{third:<10}{fourth:<10}')
