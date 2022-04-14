value = input('Enter year of birth: ')
yob = int(value)

age = 2022 - yob
print('Your age is', age, sep=': ')
print('You are', age, 'years old')
#print('You are' + str(age) + 'years old')

print('Your age is: ', end='')
print(age)

