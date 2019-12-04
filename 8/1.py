# coding=utf-8
def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if b == 0:
        solution = "x = {0}".format(float(-c) / a)
    elif a == 0 and c != 0:
        raise ValueError("Equation hasn't solve!")
    elif c == 0:
        solution = "0 = 0 (równanie jest prawdziwe dla dowolnych x, y)"
    else:
        solution = "y = {0}*x + ({1})".format(-float(a) / float(b), -float(c) / float(b))
    return solution


s1 = solve1(-2, 1, 3)
print s1
assert "y = 2.0*x + (-3.0)" == s1
