import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    if N <= 3:
        print(1)
    else:
        dp = [0] * (N + 1)
        dp[1], dp[2], dp[3] = 1, 1, 1
        for i in range(4, N+1):
            dp[i] = dp[i-3] + dp[i-2]
        print(dp[N])