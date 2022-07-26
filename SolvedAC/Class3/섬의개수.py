from collections import deque
import sys

dr = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]


def oob(row, col, nr, nc):
    if 0 <= nr < row and 0 <= nc < col:
        return True
    return False


def bfs(row, col, guidance):
    visited = [[False]*col for _ in range(row)]
    island = 0
    for r in range(row):
        for c in range(col):
            if not visited[r][c]:
                # print("방문 노드 : {}, {}".format(r, c))
                visited[r][c] = True
                if guidance[r][c] == 1:
                    queue = deque([(r, c)])
                    while queue:
                        node = queue.popleft()
                        for i in range(9):
                            nr = node[0] + dr[i]
                            nc = node[1] + dc[i]
                            if oob(row, col, nr, nc) and not visited[nr][nc]:
                                visited[nr][nc] = True
                                if guidance[nr][nc] == 1:
                                    queue.append((nr, nc))
                    # print(visited)
                    island += 1

    return island


while True:

    W, H = map(int, sys.stdin.readline().split())
    if W == 0 and H == 0:
        break
    guidance = [[0]*W for _ in range(H)]
    for h in range(H):
        arr = list(map(int, sys.stdin.readline().split()))
        guidance[h] = arr

    print(bfs(H, W, guidance))