import random

def guess(x):
    random_number = random.randint(1, 50)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Guess again. Too low.')
        elif guess > random_number:
            print('Guess again. Too high.')
        elif guess == random_number:
            print(f'Congratulations. You guessed the number {random_number}')

guess(50)

def guess(y):
    superrandomnumber = random.randint(-999, 999)
    guess = 0
    while guess != superrandomnumber:
        guess = int(input(f'Guess a number, if you can.'))
        if guess < superrandomnumber:
            print('Guess again. Too low.')
        elif guess > superrandomnumber:
            print('Guess again. Too high.')
        elif guess == superrandomnumber:
            print(f'Well done. But how about this?')

guess(50)

def guess(z):
    superduperrandomnumber = random.randint(-9999, 9999)
    guess = 0
    while guess != superduperrandomnumber:
        guess = int(input(f'Guess a number, if you can.'))
        if guess < superduperrandomnumber:
            print('Guess again. Too low.')
        elif guess > superduperrandomnumber:
            print('Guess again. Too high.')
        elif guess == superduperrandomnumber:
            print(f'Well done. Well done.')

guess(50)