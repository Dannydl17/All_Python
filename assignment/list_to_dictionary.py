def can_convert_list_to_dictionary(param):
    dictionary = {}
    for count in param:
        result = count[0]
        if result in dictionary:
            result = count[0].upper()
        dictionary[result] = count
    return dictionary
