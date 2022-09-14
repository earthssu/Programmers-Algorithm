import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    distance = [0] * (N+1)
    visited = [False] * (N+1)
    queue = deque([start])

    while queue:
        node = queue.popleft()
        visited[node] = True
        for i in graph[node]:
            if not visited[i]:
                distance[i] = distance[node] + 1
                queue.append(i)

    return sum(distance)


result = []
for i in range(1, N+1):
    result.append(bfs(i))

print(result.index(min(result))+1)