def reversal_it(L, left, right):
    rng = range(len(L))
    if right not in rng or left not in rng:
        raise Exception("Index out of bounds")
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return L


def reversal_rec(L, left, right):
    rng = range(len(L))
    if right not in rng or left not in rng:
        raise Exception("Index out of bounds")
    elif left > right:
        return L
    L[right], L[left] = L[left], L[right]
    return reversal_rec(L, left + 1, right - 1)


L = range(10)
print reversal_it(L, 4, 9)
L = range(10)
print reversal_rec(L, 4, 9)
