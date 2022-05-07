grades = []
while True:
    x = int(input('Enter grade: '))
    if x < 0 or x > 20:
        continue
    if x == 0:
        break
    grades += [x]

# Version 1
f = False
for g in grades:
    if g < 9.5:
        f = True
        break

if not f:
    print('Not found!')

# Version 2
for g in grades:
    if g < 9.5:
        break
else:
    print('Not found!')

# Version 3
for i, g in enumerate(grades, 1):
    if g < 9.5:
        print(i)
        break
else:
    print('Not found!')
