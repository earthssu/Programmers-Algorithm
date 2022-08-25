import sys

M = int(sys.stdin.readline())
for _ in range(M):
    N = int(sys.stdin.readline())
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, sys.stdin.readline().split())))

    if N > 1:
        sticker[0][1] += sticker[1][0]
        sticker[1][1] += sticker[0][0]

        for i in range(2, N):
            sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
            sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])

    print(max(sticker[0][N-1], sticker[1][N-1]))