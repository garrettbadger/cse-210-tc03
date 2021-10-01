import random


def number_game():
    number = random.randint(0, 100)
    guess = -1
    while guess != number:
        guess = int(input("What is your guess? :"))
        if guess > number:
            print("Your guess is too high!")
        elif guess < number:
            print("Your guess is too low!")
    else:
        print("Congratulations you guessed the number!")
        print("Thanks for playing!")
