S = 0
while (x := int(input('Enter number: '))) != 0:
    if x < 0:
        continue
    S += x

print(S)

print('-' * 50)

S = 0
while (True):
    x = int(input('Enter a number: '))
    if x < 0:
        continue
    elif x == 0:
        break
    S += x

print(S)
