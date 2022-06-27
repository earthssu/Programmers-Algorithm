import sys


def fibonacci(n):
    arr_fir = [1, 0]
    arr_sec = [0, 1]
    if n == 0:
        return arr_fir
    elif n == 1:
        return arr_sec
    else:
        for i in range(2, n+1):
            arr_sec, arr_fir = [x + y for x, y in zip(arr_fir, arr_sec)], arr_sec
        return arr_sec


N = int(sys.stdin.readline())
for i in range(N):
    num = int(sys.stdin.readline())
    arr = fibonacci(num)
    print(arr[0], arr[1])