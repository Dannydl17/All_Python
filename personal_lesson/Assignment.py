def password_validator():
    while True:
        password = input("Enter a valid password: ")
        invalid_inputs = []

        if len(password) < 8:
            invalid_inputs.append("Password should have at least eight characters: ")

        if not any(char.isdigit() for char in password):
            invalid_inputs.append("Password should have at least one number")

        if not any(char.islower() for char in password):
            invalid_inputs.append("Password should have at least a lowercase letter")

        if not any(char.isupper() for char in password):
            invalid_inputs.append("Password should have at least an uppercase letter")

        if not invalid_inputs:
            return password
        else:
            print("Invalid password. The following error were found;")
            for invalid_input in invalid_inputs:
                print(invalid_input)


valid_input = password_validator()
print(valid_input)
