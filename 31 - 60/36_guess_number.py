import random

def guess_number():
    target = random.randint(1, 10)
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == target:
            print("Correct!")
            break
        print("Try again!")

guess_number()