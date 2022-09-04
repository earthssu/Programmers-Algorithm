import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
box = []
for _ in range(N):
    box.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
day = 0

queue = deque([])
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))

while queue:
    node = queue.popleft()
    for n in range(4):
        nr = node[0] + dx[n]
        nc = node[1] + dy[n]
        if 0 <= nr < N and 0 <= nc < M:
            if box[nr][nc] == 0:
                queue.append((nr, nc))
                box[nr][nc] += box[node[0]][node[1]] + 1

flag = False
for n in range(N):
    for m in range(M):
        if box[n][m] == 0:
            flag = True
            break

if flag:
    print(-1)
else:
    print(max(map(max, box)) - 1)