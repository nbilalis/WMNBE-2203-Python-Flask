import random

print(random.random()) 			# [0, 1) float

x = random.randint(1, 6)		# [1, 6] int
y = random.randint(1, 6)		# [1, 6] int

print('Dice results', x, y, sep=' : ')
