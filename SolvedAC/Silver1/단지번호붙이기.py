import sys
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(sys.stdin.readline())
town = []
for _ in range(N):
    town.append(list(map(int, sys.stdin.readline().strip())))

cnt = 0
danji = []
for i in range(N):
    for j in range(N):
        if town[i][j] == 1:
            queue = deque([(i, j)])
            town[i][j] = -1
            while queue:
                node = queue.popleft()
                cnt += 1
                for k in range(4):
                    nr = node[0] + dr[k]
                    nc = node[1] + dc[k]
                    if 0 <= nr < N and 0 <= nc < N and town[nr][nc] == 1:
                        queue.append((nr, nc))
                        town[nr][nc] = -1
            danji.append(cnt)
            cnt = 0

danji.sort()
print(len(danji))
for d in danji:
    print(d)