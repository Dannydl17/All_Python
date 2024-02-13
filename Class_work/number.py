def skip_number() -> int:
    number = 0
    while number <= 6:
        if number != 3 and number != 6:
            number += 1


print(skip_number())
