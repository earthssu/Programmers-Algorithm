import math


def prime_factors(num):
    result = []
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            count = 0
            while num % i == 0:
                count += 1
                num //= i
            result.append((i, count))
    if num > 1:
        result.append((num, 1))
    return result