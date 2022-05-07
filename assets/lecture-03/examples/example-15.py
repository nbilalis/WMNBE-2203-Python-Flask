def minmax(list):
    min = max = list[0]

    for x in list[1:]:
        if x < min:
            min = x
        if x > max:
            max = x

    return min, max


res = minmax([3, 7, 4, 9, 6])

print(res, type(res))
