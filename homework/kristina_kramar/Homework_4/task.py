my_dict = {
    'tuple': (7, 'apple', 3.14, True, None),
    'list': [42, 'cat', 9.81, False, 'hello'],
    'dict': {'a': 1, 'b': 'text', 'c': 2.5, 'd': True, 'e': None},
    'set': {5, 'dog', 1.23, False, 'world'}
}

print(my_dict['tuple'][-1])

my_dict['list'].append(5)
my_dict['list'].pop(2)

my_dict['dict']['i am a tuple'] = 'good'
my_dict['dict'].pop('a')

my_dict['set'].add('mouse')
my_dict['set'].discard('dog')

print(my_dict)
