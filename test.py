L = [-4, 9, -9, -6, 1, -2, 1, -1]

def positive_product(L):
    print(L)
    if len(L) == 2:
        return L[0] * L[1] > 0
    elif L[0] > 0:
        return positive_product(L[1:])
    else:
        return not positive_product(L[1:])


print(positive_product(L))


