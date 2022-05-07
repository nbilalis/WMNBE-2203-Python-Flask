S = 0
while S <= 100:
    x = int(input('Enter a number: '))
    S += x

print('-' * 50)

S = 0
while S <= 100:
    x = int(input('Enter a number: '))
    if (x <= 0):
        break
    S += x
else:
    print('Done!')
