name = 'string'


def to_add(name):
    word = name[::1]
    print(word)
    result = ''
    nams = len(word)
    if nams < 3:
        return name
    else:
        var = word[-3::]

    if var == "ing":
        name += "ly"
    else:
        name += 'ing'
    return name


print(to_add(name))
