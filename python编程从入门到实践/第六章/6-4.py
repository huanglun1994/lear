# -*- coding: utf-8 -*-
keys_mean = {
    'for': 'circulation',
    'if': 'condition testing',
    'print': 'output',
    'int': 'integer',
    'break': 'exit a loop',
}
for key, mean in keys_mean.items():
    print(key + ': ' + mean)
keys_mean['in'] = 'check whether there exists'
keys_mean['def'] = 'definition'
keys_mean['del'] = 'delete'
keys_mean['lambda'] = 'anonymous function'
keys_mean['return'] = 'get a value'
print('\nNew dictory is:')
print(keys_mean)
for key, mean in keys_mean.items():
    print(key + ': ' + mean)