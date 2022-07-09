import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = dict()

for n in range(1, N+1):
    graph[n] = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visit = []
stack = [V]
while stack:
    node = stack.pop()
    if node not in visit:
        visit.append(node)
        graph[node].sort(reverse=True)
        stack.extend(graph[node])

for v in visit:
    print(v, end=' ')
print()

visit = []
queue = deque([V])
while queue:
    node = queue.popleft()
    if node not in visit:
        visit.append(node)
        graph[node].sort()
        queue.extend(graph[node])

for v in visit:
    print(v, end=' ')

