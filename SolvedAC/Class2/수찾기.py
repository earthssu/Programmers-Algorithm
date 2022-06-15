import sys


def binary_search(arr, num):
    start = 0
    end = len(arr) - 1
    mid = (start + end) // 2

    while start <= end:
        if arr[mid] == num:
            return True
        elif arr[mid] > num:
            end = mid - 1
        elif arr[mid] < num:
            start = mid + 1
        mid = (start + end) // 2

    return False


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))

arr.sort()

M = int(sys.stdin.readline())
search = list(map(int, sys.stdin.readline().split(" ")))

for s in search:
    if binary_search(arr, s):
        print(1)
    else:
        print(0)