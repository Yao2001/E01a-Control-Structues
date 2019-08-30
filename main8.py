#!/usr/bin/env python3

import utils

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')
color = ''
while (color != 'black'):
    color = input("What is my favorite color? ")
    color = color.lower().strip()
    if (color == 'black'):
        print('Yes!')
    elif (color == 'white'):
        print('Not even close!')
    else:
        print('I do not like it.')