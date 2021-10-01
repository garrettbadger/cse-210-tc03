import random
def garrettbadger():
    print('Hello from Garrett Badger!')

number = random.randint(0, 100)
def random(number):
    guess = -1
    while guess != number:
        guess = input("What is your guess? :")
        if guess > number:
            print("Your guess is too high!")
        elif guess < number:
            print("Your guess is too low!")
    else:
        print("Congratulations you guessed the number!")
        print("Thanks for playing!")
random(number)