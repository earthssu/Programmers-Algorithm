"""
막대기의 길이에 따라 가격이 다를 때,
최고의 수익을 얻도록 막대기를 자른다면 그 가격은
"""
def solution(price, n):
    dp = [0] * (n+1)
    max_value = 0
    for i in range(1, n+1):
        for j in range(i):
            max_value = max(max_value, price[i-j]+dp[j])
        dp[i] = max_value
    return dp[n]