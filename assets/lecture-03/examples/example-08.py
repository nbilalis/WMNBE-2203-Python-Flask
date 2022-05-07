S = 0
while S <= 100:
    x = int(input('Enter a number: '))
    if x <= 0:
        continue
    S += x

print('-' * 50)

S = 0
while S <= 100:
    x = int(input('Enter a number: '))
    if x > 0:
        S += x
