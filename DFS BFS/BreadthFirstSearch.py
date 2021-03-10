from collections import deque

def bfs(graph, start_node):
    visit = []
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit
