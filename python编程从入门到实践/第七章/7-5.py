# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
while True:
    prompt = '\nPlease enter your age:'
    prompt += '\nEnter quit to exit promgram. '
    age = input(prompt)
    if age == 'quit':
        break
    elif int(age) < 3:
        print('You can watch the movie for free!')
    elif 3 <= int(age) <= 12:
        print('Your ticket price is ten dollars.')
    elif int(age) > 12:
        print('Your ticket price is fifteen dollars.')