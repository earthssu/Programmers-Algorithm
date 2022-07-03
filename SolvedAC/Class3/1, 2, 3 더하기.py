import sys


N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    arr = [0, 1, 2, 4]
    if num < 4:
        print(arr[num])
    else:
        for j in range(4, num+1):
            arr.append(arr[j-1] + arr[j-2] + arr[j-3])
        print(arr[num])