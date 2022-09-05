import sys
from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

N = int(sys.stdin.readline())

for _ in range(N):
    I = int(sys.stdin.readline())
    night = tuple(map(int, sys.stdin.readline().split()))
    final = list(map(int, sys.stdin.readline().split()))
    visited = [[0]*I for _ in range(I)]
    queue = deque([night])
    count = 0
    while queue:
        node = queue.popleft()
        if node[0] == final[0] and node[1] == final[1]:
            print(visited[final[0]][final[1]])
            break

        for i in range(8):
            nr = node[0] + dx[i]
            nc = node[1] + dy[i]
            if 0 <= nr < I and 0 <= nc < I and visited[nr][nc] == 0:
                visited[nr][nc] += visited[node[0]][node[1]] + 1
                queue.append((nr, nc))
