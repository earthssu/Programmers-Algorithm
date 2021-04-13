from collections import deque


def bfs(v, visited, adj):
    count = 0
    q = deque([[v, count]])  # [node, 거리]
    while q:
        value = q.popleft()
        v = value[0]
        count = value[1]
        if visited[v] == -1:
            visited[v] = count  # 방문 완료 노드에 거리 저장
            count += 1  # 그 다음 노드부터는 거리가 1 증가하므로
            for e in adj[v]:  # 현재 노드와 연결된 노드들
                q. append([e, count])


def solution(n, edge):
    answer = 0
    visited = [-1] * (n + 1)
    adj = [[] for _ in range(n + 1)]

    for e in edge:
        x, y = e[0], e[1]
        adj[x].append(y)
        adj[y].append(x)

    bfs(1, visited, adj)

    for value in visited:
        if value == max(visited):
            answer += 1

    return answer