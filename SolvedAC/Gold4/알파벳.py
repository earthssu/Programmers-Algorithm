import sys
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

R, C = map(int, sys.stdin.readline().split())
graph = []
for _ in range(R):
    graph.append(list(sys.stdin.readline().strip()))

used = [False] * 26
used[ord(graph[0][0])-65] = True
answer = 0

def dfs(count, used, r, c):
    global answer
    answer = max(count, answer)
    
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if 0 <= nr < R and 0 <= nc < C and not used[ord(graph[nr][nc])-65]:
            used[ord(graph[nr][nc])-65] = True
            dfs(count+1, used, nr, nc)
            used[ord(graph[nr][nc])-65] = False

dfs(1, used, 0, 0)
print(answer)
