import sys


N = int(sys.stdin.readline())
arr = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().strip().split(" "))
    arr.append((a, b))

result = sorted(arr)
for a, b in result:
    print(a, b)