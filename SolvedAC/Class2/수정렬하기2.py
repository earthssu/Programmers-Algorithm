import sys


N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()
for a in arr:
    print(a)