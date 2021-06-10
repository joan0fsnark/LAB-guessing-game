"""A number-guessing game."""

from random import randint

print('Hello!')
name = input('What is your name?   > ')
name = name.capitalize()
print(f'{name}, pick a number between 1 and 100.')

rand_num = randint(0, 100)
tries = 0

while True:
    guess = input('What is your guess?  > ')

    # Make sure the guess is actually a number
    try:
        guess = int(guess)
    except ValueError:
        print(f'"{guess}" is not a valid number, try again.')
        continue

    # Make sure the guess is between 1 and 100
    if guess < 1 and guess > 100:
        print('Number must be between 1 and 100.')
        continue

    tries += 1

    if guess > rand_num:
        print('Too high.')
    elif guess < rand_num:
        print('Too low.')
    else:
        print(f'Congratulations, {name}! You guessed it in {tries} tries.')
        break
