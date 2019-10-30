romans = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
ints = [1, 5, 10, 50, 100, 500, 1000]

dictionary = dict(zip(romans, ints))


def roman2int(roman):
    int_value = 0
    for i in range(len(roman)):
        if i > 0 and dictionary[roman[i]] > dictionary[roman[i - 1]]:
            int_value += dictionary[roman[i]] - 2 * dictionary[roman[i - 1]]
        else:
            int_value += dictionary[roman[i]]
    return int_value


example = ['XIX', 'XCV', 'MXXV']
example_result = [19, 95, 1025]
results = dict(zip(example, example_result))
for el in results:
    assert results[el] == roman2int(el)
