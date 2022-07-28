import sys

M = int(sys.stdin.readline())
relation = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
graph = {}
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a not in graph.keys():
        graph[a] = [b]
    else:
        graph[a].append(b)
    if b not in graph.keys():
        graph[b] = [a]
    else:
        graph[b].append(a)

visited = [False] * (M + 1)
result = []


def DFS(node, num):
    num += 1
    visited[node] = True

    if node == relation[1]:
        result.append(num)
    else:
        for n in graph[node]:
            if not visited[n]:
                DFS(n, num)


DFS(relation[0], 0)

if len(result) > 0:
    print(result[0]-1)
else:
    print(-1)