# -*- coding: utf-8 -*-
my_girlfriend = {
    'relationship': "My girlfriend's",
    'first_name': 'Wang',
    'last_name': 'Di',
    'age': 23,
    'city': 'Cheng Du',
}
me = {
    'relationship': 'My',
    'first_name': 'Huang',
    'last_name': 'Lun',
    'age': 23,
    'city': 'Cheng Du',
}
my_friend = {
    'relationship': "My friend's",
    'first_name': 'Ran',
    'last_name': 'Ming',
    'age': 24,
    'city': 'Ning Bo',
}
people = [me, my_girlfriend, my_friend]
for person in people:
    print('\n' + person['relationship'] + " first_name is " + person['first_name'] + '.')
    print(person['relationship'] + " last_name is " + person['last_name'] + '.')
    print(person['relationship'] + " age is " + str(person['age']) + '.')
    print(person['relationship'] + " city is " + person['city'] + '.')