def find_outlier(integ):
    sam = integ[:3]
    even = sum(1 for x in sam if x % 2 == 0)
    odd = 3 - even

    if even > odd:
        return next(x for x in integ if x % 2 != 0)
    else:
        return next(x for x in integ if x % 2 == 0)
    

print(find_outlier([-4207752, 362590, 5205484, 11340, 3740336, 1360605]))