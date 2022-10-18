import sys

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0
visited = [[False] * M for _ in range(N)]

def dfs(count, total, r, c):
    global answer
    if count == 4:
        answer = max(total, answer)
        return
    
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(count+1, total+graph[nr][nc], nr, nc)
            visited[nr][nc] = False

def plus(r, c):
    global answer
    for n in range(4):
        total = graph[r][c]
        for k in range(3):
            i = (n+k) % 4
            nr = r + dx[i]
            nc = c + dy[i]
            if not (0 <= nr < N and 0 <= nc < M):
                total = 0
                break
            total += graph[nr][nc]
        answer = max(total, answer)
    

for n in range(N):
    for m in range(M):
        if not visited[n][m]:
            visited[n][m] = True
            dfs(1, graph[n][m], n, m)
            visited[n][m] = False
            plus(n, m)

print(answer)
