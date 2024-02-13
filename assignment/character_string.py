def count_string_and_return_dictionary(words):
    dictionary = {}

    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary
