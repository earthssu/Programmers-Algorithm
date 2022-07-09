import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sequence = [1] * N

for cur, val in enumerate(arr):
    for pre in range(cur):
        if arr[pre] < val:
            sequence[cur] = max(sequence[cur], sequence[pre] + 1)

print(max(sequence))