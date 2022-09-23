def GCD(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b


def LCM(a, b):
    return a * b // GCD(a, b)