import sys

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
result = [0] * N

for i in range(N):
    result[i] = 1
    for j in range(0, i):
        if sequence[i] < sequence[j]:
            result[i] = max(result[i], result[j] + 1)

print(max(result))