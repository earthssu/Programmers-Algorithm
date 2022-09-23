from collections import deque


def solution(maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    N, M = len(maps), len(maps[0])
    queue = deque([(0, 0)])
    while queue:
        node = queue.popleft()
        if node[0] == N-1 and node[1] == M-1:
            return maps[N-1][M-1]
        for i in range(4):
            nr = node[0] + dx[i]
            nc = node[1] + dy[i]
            if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] == 1:
                maps[nr][nc] += maps[node[0]][node[1]]
                queue.append((nr, nc))
    return -1