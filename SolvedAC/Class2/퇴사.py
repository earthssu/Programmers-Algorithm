N = int(input())
date = []
value = []

for _ in range(N):
    d, v = map(int, input().split())
    date.append(d)
    value.append(v)

dp = [0] * (N+1)
for i in range(N-1, -1, -1):
    if date[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(value[i]+dp[i+date[i]], dp[i+1])

print(dp[0])
