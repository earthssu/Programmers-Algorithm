import sys


def primes(num):
    m = int(num ** 0.5)
    for i in range(2, m+1):
        if num % i == 0:
            return False
    return True


N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    prime_arr = primes(num)

    a, b = num // 2, num // 2
    while a > 0:
        if primes(a) and primes(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
