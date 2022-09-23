import heapq  # 우선순위 큐 구현을 위함
INF = int(1e9)
"""
한 노드에서 특정 다른 노드까지의 최단 거리 구함
음의 간선이 없어야 정상 작동
"""

node, edge = map(int, input().split())
start = int(input())

graph = [[] for _ in range(node+1)]
distance = [INF] * (node+1)

for _ in range(edge):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# print the shortest distances
for i in range(1, node + 1):
    # if not reachable, print INF
    if distance[i] == INF:
        print("INF")
    # print reachable distance
    else:
        print(distance[i])