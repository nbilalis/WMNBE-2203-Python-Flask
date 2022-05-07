for char in 'Montoya':
    print(char)

for word in ('My name is Iñigo Montoya'.split(' ')):
    print(word)

for char in 'My name is Iñigo Montoya':
    if char == 'ñ':
        print('Found!')
        break
else:
    print('Not found…')
