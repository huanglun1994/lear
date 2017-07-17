# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
active = True
while active:
    prompt = '\nPlease enter your age:'
    prompt += '\nEnter quit to exit promgram. '
    age = input(prompt)
    if age == 'quit':
        break
    elif int(age) <= 0:
        active = False
    elif 0 < int(age) < 3:
        print('You can watch the movie for free!')
    elif 3 <= int(age) <= 12:
        print('Your ticket price is ten dollars.')
    elif int(age) > 12:
        print('Your ticket price is fifteen dollars.')