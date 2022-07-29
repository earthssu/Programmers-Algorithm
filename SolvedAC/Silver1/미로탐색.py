import sys
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
N, M = map(int, sys.stdin.readline().split())
miroh = []
for i in range(N):
    miroh.append(list(map(int, sys.stdin.readline().strip())))

queue = deque([(0, 0)])

while queue:
    node = queue.popleft()
    for i in range(4):
        nr = node[0] + dr[i]
        nc = node[1] + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if miroh[nr][nc] == 1:
                miroh[nr][nc] = miroh[node[0]][node[1]] + 1
                queue.append((nr, nc))

print(miroh[N-1][M-1])