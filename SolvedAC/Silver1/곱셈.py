import sys

A, B, C = map(int, sys.stdin.readline().split())


def fpow(num, n):
    if n == 1:
        return num % C
    else:
        x = fpow(num, n//2)
        if n % 2 == 0:
            return (x * x) % C
        else:
            return (x * x * num) % C


print(fpow(A, B))
