import sys
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split())
lab = []
cand = []
vv = []
answer = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    lab.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M):
        if lab[i][j] == 0:
            cand.append((i, j))
        elif lab[i][j] == 2:
            vv.append((i, j))

used = [False] * len(cand)


def virus(room, idx, count, used):
    global answer
    if count == 3:  # 벽을 다 세웠다면 바이러스 퍼져나가는 거 검사하기
        visited = [[False] * M for _ in range(N)]
        temp = copy.deepcopy(room)
        queue = deque()
        for v in vv:
            queue.append(v)
            visited[v[0]][v[1]] = True
        while queue:
            node = queue.popleft()
            for x in range(4):
                nr = node[0] + dx[x]
                nc = node[1] + dy[x]
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and temp[nr][nc] == 0:
                    temp[nr][nc] = 2
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        total = 0
        for n in range(N):
            for m in range(M):
                if temp[n][m] == 0:
                    total += 1
        answer = max(answer, total)
        return

    for i in range(idx, len(cand)):
        if not used[i]:
            room[cand[i][0]][cand[i][1]] = 1
            used[i] = True
            virus(room, i, count+1, used)
            used[i] = False
            room[cand[i][0]][cand[i][1]] = 0


virus(lab, 0, 0, used)
print(answer)