import sys

N = int(sys.stdin.readline())
grape = []
for _ in range(N):
    grape.append(int(sys.stdin.readline()))

dp = [0] * 10000
dp[0] = grape[0]
dp[1] = grape[0] + grape[1]
dp[2] = max(grape[0]+grape[2], grape[1]+grape[2], dp[1])
for i in range(3, N):
    dp[i] = max(grape[i]+grape[i-2], grape[i]+grape[i-1]+grape[i-3], dp[i-1])

print(max(dp))