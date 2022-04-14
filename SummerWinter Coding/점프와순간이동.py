def solution(n):
    ans = 1

    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            ans += 1
            n = (n-1) / 2

    return ans