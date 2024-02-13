def is_palindrome(numbers: int):
    number = numbers
    reversed_number = 0

    while numbers != 0:
        remainder = numbers % 10
        reversed_number = reversed_number * 10 + remainder
        numbers = numbers // 10
    if number == reversed_number:
        return True
    else:
        return False


is_palindrome()
