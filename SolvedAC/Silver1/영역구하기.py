import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())
board = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

results = []
for m in range(M):
    for n in range(N):
        if board[m][n] == 0:
            board[m][n] = 1
            count = 1
            queue = deque([(m, n)])
            while queue:
                node = queue.popleft()
                board[node[0]][node[1]] = 1
                for i in range(4):
                    nr = node[0] + dx[i]
                    nc = node[1] + dy[i]
                    if 0 <= nr < M and 0 <= nc < N and board[nr][nc] == 0:
                        queue.append((nr, nc))
                        count += 1
                        board[nr][nc] = 1
            results.append(count)

print(len(results))
print(*sorted(results))