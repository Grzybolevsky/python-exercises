# P(0, 0) = 0.5,
# P(i, 0) = 0.0 dla i > 0,
# P(0, j) = 1.0 dla j > 0,
# P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.


def solve_dynamc(i, j):
    i, j = i + 1, j + 1
    value_list = {0: [0.5] + [1.0 for m in range(1, j)]}
    for n in range(1, i):
        value_list[n] = [0.0]
        for m in range(1, j):
            value_list[n].append(0.5 * (value_list[n - 1][m] + value_list[n][m - 1]))
    return value_list[i - 1][j - 1]


def solve_recursive(i, j):
    if i == 0 and j == 0:
        return 0.5
    elif i != 0 and j == 0:
        return 0.0
    elif i == 0 and j != 0:
        return 1.0
    else:
        return 0.5 * (solve_recursive(i - 1, j) + solve_recursive(i, j - 1))


def get_array(i, j, func):
    arr = dict()
    for n in range(i + 1):
        arr[n] = [func(n, 0)]
        for m in range(1, j + 1):
            arr[n].append(func(n, m))
    return arr


if __name__ == '__main__':
    i, j = 2, 4

    value_dynamic = solve_dynamc(i, j)
    value_recursive = solve_recursive(i, j)
    recursive_array = get_array(i, j, solve_recursive)
    dynamic_array = get_array(i, j, solve_dynamc)

    print recursive_array
    print dynamic_array
    print value_dynamic
    print value_recursive
