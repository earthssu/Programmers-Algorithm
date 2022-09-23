"""
모든 지점에서 모든 지점으로의 최단 경로 구함
"""
INF = int(1e9)

node, edge = map(int, input().split())

graph = [[INF]*(node+1) for _ in range(node+1)]
for a in range(1, node+1):
    for b in range(1, node+1):
        if a == b:
            graph[a][b] = 0

for _ in range(edge):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, node+1):
    for a in range(1, node+1):
        for b in range(1, node+1):
            graph[a][b] = min(graph[a][k]+graph[k][b], graph[a][b])