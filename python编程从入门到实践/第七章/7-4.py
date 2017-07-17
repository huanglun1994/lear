# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
while True:
    prompt = '\nPlease tell me what kind of toppings would you like to add?'
    prompt += '\nEnter quit to exit program. '
    pizza_toppings = input(prompt)
    if pizza_toppings == 'quit':
        break
    else:
        print('I will add ' + pizza_toppings + ' to your pizza.')