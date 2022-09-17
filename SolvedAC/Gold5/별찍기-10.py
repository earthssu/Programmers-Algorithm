import sys

N = int(sys.stdin.readline())
maps = [[' '] * N for _ in range(N)]


def stars(row, col, size):
    if size == 3:
        for i in range(row, row+3):
            for j in range(col, col+3):
                if i != row+1 or j != col+1:
                    maps[i][j] = "*"
        return

    s = size // 3
    stars(row, col, s)
    stars(row, col+s, s)
    stars(row, col+s+s, s)
    stars(row+s, col, s)
    stars(row+s, col+s+s, s)
    stars(row+s+s, col, s)
    stars(row+s+s, col+s, s)
    stars(row+s+s, col+s+s, s)


stars(0, 0, N)
for i in range(N):
    for j in range(N):
        print(maps[i][j], end='')
    print()