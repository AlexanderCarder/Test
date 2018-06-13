import random

print('--------------------------------------')
print('        GUESS THAT NUMBER GAME        ')
print('--------------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1
number_of_guesses = 0

while guess != the_number:
    number_of_guesses += 1
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Your guess of {0} was too LOW.'.format(guess))
    elif guess > the_number:
        print('Your guess of {0} was too HIGH.'.format(guess))
    else:
        print('You win!')

print('Number of guesses: ' + str(number_of_guesses))