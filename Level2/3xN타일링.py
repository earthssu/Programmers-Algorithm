def solution(n):
    if (n * 3) % 2 == 1:
        return 0

    dp = [0] * (n + 1)
    dp[2] = 3
    if n > 2:
        dp[4] = 11
        for i in range(6, n + 1):
            dp[i] = dp[i - 2] * 3
            for j in range(i - 4, 1, -2):
                dp[i] += dp[j] * 2
            dp[i] += 2

    return dp[n] % 1000000007