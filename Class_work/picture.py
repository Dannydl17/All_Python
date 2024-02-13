picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]
def pixel(picture: list):
    formatted_picture = ''
    for numbers in picture:
        for number in numbers:
            if number == 1:
                formatted_picture += '*'
            elif number == 0:
                formatted_picture += ' '
        formatted_picture += '\n'
    return formatted_picture

print(pixel(picture))