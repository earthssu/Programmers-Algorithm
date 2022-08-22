import sys


def hanoi(n, start, end):
    tmp = 6 - start - end
    if n == 1:
        print(start, end)
        return

    hanoi(n-1, start, tmp)
    print(start, end)
    hanoi(n-1, tmp, end)


N = int(sys.stdin.readline())
print(2**N - 1)
hanoi(N, 1, 3)
