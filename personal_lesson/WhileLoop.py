import random

rand_ = random.randint(1, 10)
guess_number = int(input('Enter a guess number: '))
if rand_ != guess_number:
    print("Try again......")
while rand_:
    guess_number = int(input('Enter a guess number: '))
    if guess_number == rand_:
        print("You are correct")
        break
    else:
        print("Try again......")
