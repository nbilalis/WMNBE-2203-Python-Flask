x = int(input('Please enter a number: '))

if x > 0:
    print('x is positive')
else:
    print('x is negative or zero')

print('x is positive' if x > 0 else 'x is negative or zero')

print('x is positive') if x > 0 else print('x is negative or zero')
