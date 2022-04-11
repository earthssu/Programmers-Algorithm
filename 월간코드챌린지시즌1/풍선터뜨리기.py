def solution(a):
    result = [False for _ in range(len(a))]
    min_left, min_right = float('inf'), float('inf')
    for i in range(len(a)):
        if min_left > a[i]:
            min_left = a[i]
            result[i] = True
        if min_right > a[-1-i]:
            min_right = a[-1-i]
            result[-1-i] = True

    return sum(result)