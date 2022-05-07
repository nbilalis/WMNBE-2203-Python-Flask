# Version 1
list = []
x = int(input('Enter number: '))
while x != 0:
    if x > 0:
        list += [x]     # l.append(x)
    x = int(input('Enter number: '))

print(list)

# Version 2

list = []
while True:
    x = int(input('Enter number: '))
    if x < 0:
        continue
    if x == 0:
        break
    list += [x]

print(list)

# Version 3

list = []
while (x := int(input('Enter number: '))) != 0:     # walrus operator
    if x < 0:
        continue
    list += [x]

print(list)
