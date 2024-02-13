# roman_number = {
#     "I": 1,
#     "II": 2,
#     "III": 3,
#     "V": 5,
#     "XV": 5,
#     "X": 10,
#     "XX": 20
# }
# for k, v in roman_number.items():  ####To unpack a dictionary
#     print(f"{k}{v}", end='\n')
# print(roman_number.items())  ### Gives us the keys nd their values
# print(roman_number['II'])
# print(roman_number.get('v', 'key not found'))
# roman_number["XV"] = 15
# print(roman_number)
# roman_number['xxx'] = 30
# print(roman_number)
# del roman_number['I']
# print(roman_number)
# roman_number.update(C=100, D=500)
# print(roman_number)
roman_number1 = dict({'i': 1, 'ii': 2, 'iii': 3})
print(roman_number1)
answer = {n: n ** 2 for n in range(1, 6)}
print(answer)
# Set
set = ({1, 2, 3, 3, 4, 2, 1})
print(set)
