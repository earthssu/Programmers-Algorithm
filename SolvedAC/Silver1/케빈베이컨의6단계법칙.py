import sys
INF = int(1e9)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
distance = [INF] * (N+1)


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, N+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i] = 1

    for _ in range(N-1):
        now = get_smallest_node()
        visited[now] = True
        for next in graph[now]:
            cost = distance[now] + 1
            if cost < distance[next]:
                distance[next] = cost

result = []
for n in range(1, N+1):
    dijkstra(n)
    result.append(sum(distance[1:]))
    visited = [False] * (N + 1)
    distance = [INF] * (N + 1)

min_num = min(result)
for i in range(N):
    if min_num == result[i]:
        print(i+1)
        break