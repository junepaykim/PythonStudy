'''Guess number'''

import random
secretNumber= random.randint(1, 20)
print('The number is between 1 to 20.')

for guessTaken in range(1,7):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber :
        print('Your guess is low.')
    elif guess > secretNumber :
        print('Your guess is high')
    else :
        break

if guess == secretNumber :
    print('Correct!')
else :
    print('Wrong!!')