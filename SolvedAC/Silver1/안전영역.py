import sys

N = int(sys.stdin.readline())
town = []
h_min, h_max = 100, 1
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    h_min = min(h_min, min(tmp))
    h_max = max(h_max, max(tmp))
    town.append(tmp)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
results = []

for height in range(h_min-1, h_max):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                if town[i][j] > height:
                    stack = [(i, j)]
                    while stack:
                        node = stack.pop()
                        visited[node[0]][node[1]] = True
                        for k in range(4):
                            nr = node[0] + dx[k]
                            nc = node[1] + dy[k]
                            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and town[nr][nc] > height:
                                stack.append((nr, nc))
                    count += 1
    results.append(count)

print(max(results))