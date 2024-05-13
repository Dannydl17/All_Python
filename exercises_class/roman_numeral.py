# words = 'VI'

def can_check_number(word):
    num = 0
    number_list = []
    roman_numeral = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    for numbers in word:
        num = roman_numeral[numbers]
        number_list.append(num)
    return number_list


def sort_number():
    counter = 0
    result = can_check_number("MCMXCIV")
    for count in range(len(result)):
        index_one = count
        for index in range(index_one + 1, len(result)):
            index_two = index
            if result[index_one] > result[index_two]:
                break
            if result[index_one] < result[index_two]:
                tempo = result[index_one]
                result[index_one] = result[index]
                result[index] = tempo
    counter += 1
    return result


def calculate_number():
    count = 0
    new_list = []
    total_number = 0
    total_nums = 0
    results = sort_number()
    num = results[0]
    new_list.append(num)
    for num_one in range(0, len(results)):
        total_number = results[num_one]
        total_nums = results[num_one + 1]
        count = total_number - total_nums
        new_list.append(count)


# LVIII
# sort_number()
calculate_number()
# # dict_convert_list = [(key, value) for key, value in roman_numeral.items()]
