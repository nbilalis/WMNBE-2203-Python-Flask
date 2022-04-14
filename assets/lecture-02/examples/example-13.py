coin = input('Which coin did you buy: ')
x = int(input('How many of them: '))
y = float(input('How much did it cost (per coin): '))

# Method #1
print('Bought %d %s for €%.2f total!' % (x, coin, x * y))             # legacy

# Method #2
print('Bought {0} {1} for €{2:,.2f} total!'.format(x, coin, x * y))
print('Bought {n} {coin} for €{cost:,.2f} total!'.format(n=x, coin=coin, cost=x * y))

# Method #3
print(f'Bought {x} {coin} for €{x * y:,.2f} total!')
