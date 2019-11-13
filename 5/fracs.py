import fractions


def add_frac(frac1, frac2):  # frac1 + frac2
    if isinstance(frac1, list) and isinstance(frac2, list):
        if frac1[1] == 0 or frac2[1] == 0:
            raise Exception('Cant divide by 0')
        else:
            frac3 = [frac1[0] * frac2[1] + frac2[0] * frac1[1], frac1[1] * frac2[1]]
            e = fractions.gcd(frac3[0], frac3[1])
            if e != 0:
                return [frac3[0] / e, frac3[1] / e]
            else:
                return [0, 0]


def sub_frac(frac1, frac2):  # frac1 - frac2
    if isinstance(frac1, list) and isinstance(frac2, list):
        if frac1[1] == 0 or frac2[1] == 0:
            raise Exception('Cant divide by 0')
        else:
            frac3 = [frac1[0] * frac2[1] - frac2[0] * frac1[1], frac1[1] * frac2[1]]
            e = fractions.gcd(frac3[0], frac3[1])
            if e != 0:
                return [frac3[0] / e, frac3[1] / e]
            else:
                return [0, 0]


def mul_frac(frac1, frac2):  # frac1 * frac2
    if isinstance(frac1, list) and isinstance(frac2, list):
        if frac1[1] == 0 or frac2[1] == 0:
            raise Exception('Cant divide by 0')
        else:
            frac3 = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
            e = fractions.gcd(frac3[0], frac3[1])
            if e != 0:
                return [frac3[0] / e, frac3[1] / e]
            else:
                return [0,0]


def div_frac(frac1, frac2):  # frac1 / frac2
    if isinstance(frac1, list) and isinstance(frac2, list):
        if frac1[1] == 0 or frac2[1] == 0:
            raise Exception('Cant divide by 0')
        else:
            frac3 = [frac1[0] * frac2[1], frac1[1] * frac2[0]]
            e = fractions.gcd(frac3[0], frac3[1])
            if e != 0:
                return [frac3[0] / e, frac3[1] / e]
            else:
                return [0, 0]


def is_positive(frac):  # bool, czy dodatni
    if isinstance(frac, list):
        return frac2float(frac) >= 0


def is_zero(frac):  # bool, typu [0, x]
    if isinstance(frac, list):
        if frac[1] == 0:
            raise Exception('Cant divide by 0')
        elif frac[0] == 0:
            return True
        else:
            return False


def cmp_frac(frac1, frac2):  # frac1 > frac2 -- -1 | 0 | +1
    if isinstance(frac1, list) and isinstance(frac2, list):
        f1, f2 = frac2float(frac1), frac2float(frac2)
        if f1 > f2:
            return 1
        elif f1 == f2:
            return 0
        else:
            return -1


def frac2float(frac):  # konwersja do float
    if isinstance(frac, list):
        if frac[0] != 0 and frac[1] != 0:
            return float(frac[0]) / float(frac[1])
        else:
            raise Exception('Cant divide by 0')
    else:
        raise Exception('frac is not a list')
