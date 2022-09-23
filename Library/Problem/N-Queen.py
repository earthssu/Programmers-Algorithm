def dfs(queen, n, row):
    count = 0

    if n == row:
        return 1

    for col in range(n):
        queen[row] = col
        for x in range(row):
            if queen[x] == queen[row]:
                break
            if abs(queen[x] - queen[row]) == abs(x - row):
                break
        else:
            count += dfs(queen, n, row+1)

    return count


def solution(n):
    return dfs([0] * n, n, 0)