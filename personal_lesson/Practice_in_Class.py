# 29/08/23
import random

# print(type(2))
# print(type(2.1))
# print(type(True))
# print(type('david'))  # to know the data type the values belong to.

# print(4 + 4)
# print(6 - 4)
# print(10 * 4)
# print(40 / 4)
# print(10 // 4)
# print(10 % 4)

# in built function
# name = 'alphafed'
# print(len(name))
# String is a set of characters to know the length we use len

# 31/08/2023

# first_number = 1
# second_number = 2
# print(first_number + second_number)
# By default, the print line has backslash n
# Expression can be put in our print line

# message1 = 'hello'
# message2 = 'welcome'
# message3 = 'xplorers'
# msg = f'{message1}\n{message2}\n{message3}'
# print(msg)

# Conditional Statement
# age = int(input('Enter an age: '))
# if age < 18:
#     print('you are not eligible to enter our club....')
# elif age >= 18 and age <= 65:
#     print('you are eligible to enter our club....')
# else:
#     print('stay home....')

# 8/9/2023
# if block cannot be empty but we can put pass so that our if block will not be empty
# Example from our last_class.
# it can also be writing as
# result = "Not Eligible" if age < 18 else "Eligible"  ## ------>##Tenary Operator
# print(result)

# using match statement
# language = input("Enter your language:  ")
# match language:
#     case "Yoruba":
#         print("Welcome to ibadan")
#     case "ibo":
#         print("Welcome to anambra")
#     case "hausa":
#         print("Welcome to kano")
#     case  _:
#         print("You're not from here")
#
# score = int(input("Enter your score:  "))
# score *= 10
# result = ""
# if score >= 90 and score <= 100:
#     result = "Distinction"
# elif 80 <= score < 90:
#     result = "Excellent"
# elif score >= 70 and score < 80:
#     result = "B grade"
# elif score >= 60 and score < 70:
#     result = "C grade"
# elif score >= 50 and score < 60:
#     result = "D grade"
# elif score < 50:
#     result = "Fail, come back next time"
# print(f'your score is {score} and your result is {result}')

# We can call bool functions on zero it will give me false while other numbers will give me true
# print(bool(4))
# # For string also if i have empty bool ' ' they evaluate to false while a string that has a value it will be true
# print(bool(''))
# print(bool('fhfhfh'))
#
# name = input('Enter your name: ')
# if name:
#     print(f'your name is {name}')
# else:
#     print('no name entered')

# built tin function call random to generate random numbers
# when you do not need the variable you use underscore _
# you want to generate random numbers
# random will give us number between zero nd one ##--------->Random
# randint will give us number when we specify where the number will be between ##--------->Randint

# rand_ = random.randint(1, 21)
# _rand = random.random()
# print(_rand) print(rand_)
# when we want to do a task over and
# over again we use for loop and while loop repeat a task as long as the condition is true. You have to
# set a condition to make it false else it will continue to run
# Example

# count = 1
# while count < 11:
#     print(count, random.randint(1, 21))
#     count += 1

# your program generate random number between 1 and 10 ask the user to guess a number. Keep ask until the user guess the correct numbers

# 11/09/2023
# if i have a code that is collecting input and the user did not enter anything it is an empty string
# falsy values or truthy value
# if name != "":#------->
# if you dont known the number times you want to loop use while and if you known the number of times  you want to loop use forloop

# 14/9/2023
# For loop must an iterable word in the right side of it as long as we still have character in it
# Example
# for counter in 'chukwudi':  ###### used for string
#     print('counter')
# what should be at the right side of your for loop should be a collection
# Example for number:
# for count in range(4):
#     print('precious')

# num = 0
# while num <= 6:
#     if num != 3 and num != 6:
#         print(num, end='\t')
#     num += 1

# for n in range(7):
#     if n != 3 and n != 6:
#         print(n, end='\t')

my_list = [5, 6, 3, 4, 1, 2, 7, 8, 9, 10]


# my_list *= 2
#
#
# def my_index(my_list: list, n, ):
#     idx = 0
#     for i in range(len(my_list)):
#         if my_list[i] == n:
#             idx = i
#     return idx
#
#
# print(my_index())

def my_sort_func(my_list: list):
    for i in range(len(my_list)):
        print(i)
        for j in range(i + 1):
            if my_list[j] < my_list[i]:
                my_list[i], my_list[j] = my_list[j], my_list[i]

    return my_list


print(my_sort_func(my_list))
