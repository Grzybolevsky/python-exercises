def sum_seq(seq):
    total = 0
    for element in seq:
        if isinstance(element, (list, tuple)):
            total += sum_seq(element)
        else:
            total += element
    return total


L = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print sum_seq(L)
