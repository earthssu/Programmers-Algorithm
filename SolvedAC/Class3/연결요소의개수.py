import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
graph = dict()
for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visit = []
cnt = 0
while len(visit) < N:
    temp = list(set(list(graph.keys())) - set(visit))
    queue = deque([temp[0]])
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    cnt += 1

print(cnt)