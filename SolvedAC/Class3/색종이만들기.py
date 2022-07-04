import sys


N = int(sys.stdin.readline())
confetti = [[0] * N for _ in range(N)]
white, blue = 0, 0
for i in range(N):
    confetti[i] = list(map(int, sys.stdin.readline().split()))


def bfs(row, col, size):
    global white
    global blue
    total = 0
    for r in range(row, row+size):
        for c in range(col, col+size):
            total += confetti[r][c]
    if total == pow(size, 2):
        blue += 1
        return
    elif total == 0:
        white += 1
        return
    else:
        s = size // 2
        bfs(row, col, s)
        bfs(row + s, col, s)
        bfs(row, col + s, s)
        bfs(row + s, col + s, s)


bfs(0, 0, N)

print(white)
print(blue)
