import sys
from collections import deque

dh = [0, 0, 0, 0, 1, -1]
dn = [1, -1, 0, 0, 0, 0]
dm = [0, 0, 1, -1, 0, 0]
M, N, H = map(int, sys.stdin.readline().split())
tomato = []
queue = deque([])

for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(M):
            if temp[j][k] == 1:
                queue.append((i, j, k))
    tomato.append(temp)

while queue:
    node = queue.popleft()
    for i in range(6):
        nz = node[0] + dh[i]
        ny = node[1] + dn[i]
        nx = node[2] + dm[i]
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = tomato[node[0]][node[1]][node[2]] + 1
                queue.append((nz, ny, nx))

day = 0
for i in tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        print(j)
        day = max(day, max(j))
print(day - 1)