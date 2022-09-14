import sys

N, M = map(int, sys.stdin.readline().split())
candy = []
for _ in range(N):
    maps = list(map(int, sys.stdin.readline().split()))
    candy.append(maps)

result = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        result[i][j] = max(result[i-1][j], result[i][j-1], result[i-1][j-1]) + candy[i-1][j-1]

print(result[N][M])