def flatten(seq):
    return sum(([x] if not isinstance(x, (list, tuple)) else flatten(x) for x in seq), [])


sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print flatten(sequence)
