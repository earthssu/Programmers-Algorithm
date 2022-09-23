"""
모든 노드를 방문하고자 할 때
"""
def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, v, visited)