#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')
colors = ['black','white','yellow','pink','grey','blue','purple']
play_again = ''
best_count = 10            # the biggest number
while (play_again != 'n' and play_again != 'no'):
    match_color = 'black' #random.choice(colors)
    count = 0
    color = ''
    while (color != match_color):
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()
        count += 1
        if (color == match_color):
            print('Yes!')
        else:
            print('I do not like it. You have guessed {guesses} times.'.format(guesses=count))
    print('\nYou guessed it in {0} times!'.format(count))
    if (count < best_count):
        print('This is the closest so far!')
        best_count = count
    play_again = input("\n Do you want to do it again? ").lower().strip()
print('Thanks for playing!')