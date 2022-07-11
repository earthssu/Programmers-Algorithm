import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
total = [0] * N
total[0] = arr[0]

for i in range(1, N):
    total[i] = max(arr[i], arr[i] + total[i-1])

print(max(total))