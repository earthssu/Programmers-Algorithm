import sys

N = int(sys.stdin.readline())
dp = [[0]*10 for _ in range(N+1)]
for i in range(0, 10):
    dp[1][i] = 1

for n in range(2, N+1):
    for i in range(10):
        for j in range(i, 10):
            dp[n][i] += dp[n-1][j]

print(sum(dp[N]) % 10007)