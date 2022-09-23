from collections import deque
"""
두 노드 사이의 최단경로, 임의의 경로 찾고 싶을 때
"""
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[node]:
                queue.append(i)
                visited[i] = True