import sys

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
result = [0] * N

for i in range(0, N):
    result[i] = sequence[i]
    for j in range(0, i):
        if sequence[i] > sequence[j]:
            result[i] = max(result[i], sequence[i]+result[j])

print(max(result))
