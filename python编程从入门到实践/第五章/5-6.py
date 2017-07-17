# -*- coding: utf-8 -*-
age = 23
if age < 2:
    print('This man is a baby.')
elif 2 <= age < 4:
    print('This man is a toddle.')
elif 4 <= age < 13:
    print('This man is a child.')
elif 13 <= age < 20:
    print('This man is a teenager.')
elif 20 <= age < 65:
    print('This man is a adult.')
elif age >= 65:
    print('This man is the aged.')