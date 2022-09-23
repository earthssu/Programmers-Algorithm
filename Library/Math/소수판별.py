import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        return True


"""
에라토스테네스의체로 소수 구하기
"""
def eratos():
    array = [True] * 10000
    m = 100
    for i in range(2, m + 1):
        if array[i]:
            for j in range(i + i, 10000, i):
                array[j] = False
