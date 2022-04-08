def solution(n):
    answer = []
    arr = [[0] * i for i in range(1, n+1)]

    cnt = 1
    x, y = -1, 0
    while n > 0 :
        for i in range(n):
            x += 1
            arr[x][y] = cnt
            cnt += 1
        for j in range(n-1):
            y += 1
            arr[x][y] = cnt
            cnt += 1
        for j in range(n-2):
            x -= 1
            y -= 1
            arr[x][y] = cnt
            cnt += 1
        n -= 3

    for a in arr:
        answer.extend(a)
    return answer