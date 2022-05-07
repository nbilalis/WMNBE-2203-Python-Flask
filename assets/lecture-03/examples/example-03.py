name = input('Enter name: ')

# Version 1
if name == 'Alice':
    print('Hello Alice!')
elif name == 'Bob':
    print('Hello Bob!')
else:
    print("I don't know you!")

# Version 2
if name == 'Alice' or name == 'Bob':
    print(f'Hello ' + name + '!')
else:
    print("I don't know you!")

# Version 3
if name in ['Alice', 'Bob']:
    print('Hello ' + name + '!')
else:
    print("I don't know you!")

# Version 4
if name in ['Alice', 'Bob']:
    print(f'Hello {name}!')     # {{{name}}}
else:
    print('I don\'t know you!')
