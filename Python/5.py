def arr(a,b):
    return [i for i in a if i not in b]

print(arr([-8, -2, -4, 13, 10, -12, -3, 6], [-3, 17]))