# -*- coding: utf-8 -*-
my_pizzas = ['hawaii', 'marinara', 'vegetarian']
friend_pizzas = my_pizzas[:]
my_pizzas.append('capricciosa')
friend_pizzas.append('focaccia')
print('My favorite pizzas are:')
for my_pizza in my_pizzas:
    print(my_pizza)
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)