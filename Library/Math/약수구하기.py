import math


def find_all_divisors(num):
    result = []
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            result.append(i)
            if i * i != num:
                result.append(num // i)
    return result