def dfs(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if com != connect and computers[com][connect] == 1:
            if not visited[connect]:
                dfs(n, computers, connect, visited)


def bfs(n, computers, com, visited):
    visited[com] = True
    queue = [com]
    while queue:
        com = queue.pop(0)
        visited[com] = True
        for connect in range(n):
            if com != connect and computers[com][connect] == 1:
                if not visited[connect]:
                    queue.append(connect)


def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            dfs(n, computers, com, visited)
            # bfs(n, computers, com, visited)
            answer += 1
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))