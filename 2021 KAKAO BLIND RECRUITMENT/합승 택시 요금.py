import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances


def solution(n, s, a, b, fares):
    answer = []
    fee_dic = {}
    for i in range(n):
        fee_dic[i+1] = {}

    for f in fares:
        fee_dic[f[0]][f[1]] = f[2]
        fee_dic[f[1]][f[0]] = f[2]

    candidate = dijkstra(fee_dic, s)
    answer.append(candidate[a] + candidate[b])
    for i in range(1, n+1):
        if i == s:
            continue
        mid = i
        temp = dijkstra(fee_dic, mid)
        answer.append(candidate[mid] + temp[a] + temp[b])

    return min(answer)
