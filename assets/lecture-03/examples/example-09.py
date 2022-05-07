s = 'My name is Iñigo Montoya'

i = 0
while i < len(s):
    if (s[i] == 'ñ'):
        print('Found at pos: ', i)
        break
    i += 1
else:
    print('Not found')
