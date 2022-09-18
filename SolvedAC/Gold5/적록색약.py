import sys

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
N = int(sys.stdin.readline())
rgb_map = []
for _ in range(N):
    rgb_map.append(list(sys.stdin.readline().strip()))
visited = [[False]*N for _ in range(N)]


def rgb_dfs(row, col):
    queue = [(row, col)]
    while queue:
        node = queue.pop()
        visited[node[0]][node[1]] = True
        for k in range(4):
            nr = node[0] + dr[k]
            nc = node[1] + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and rgb_map[nr][nc] == rgb_map[node[0]][node[1]]:
                queue.append((nr, nc))


three_p = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            rgb_dfs(i, j)
            three_p += 1

for i in range(N):
    for j in range(N):
        visited[i][j] = False
        if rgb_map[i][j] == 'G':
            rgb_map[i][j] = 'R'

two_p = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            rgb_dfs(i, j)
            two_p += 1

print(three_p, two_p)