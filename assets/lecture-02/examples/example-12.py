s = "1,2,3,4,5,6,7"

l = s.split(',')
print(l)
print(type(l))

# Unpacking
[first, second] = "SAE Group".split(" ")
print(first)
print(second)

s = "-".join([first, second])
print(s)
