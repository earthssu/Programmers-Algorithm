import sys

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for row in graph:
    for i in range(N):
        print(row[i], end=' ')
    print()