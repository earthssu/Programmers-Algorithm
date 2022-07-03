import sys


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    land = [[0] * M for i in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        land[y][x] = 1

    visit = []
    result = 0
    for n in range(N):
        for m in range(M):
            if (n, m) not in visit and land[n][m] == 1:  # 땅에 배추가 있으면 탐색
                queue = [(n, m)]  # bfs 시작
                while queue:
                    node = queue.pop()
                    visit.append(node)

                    for d in range(4):
                        dn = node[0] + dx[d]
                        dm = node[1] + dy[d]
                        if 0 <= dn < N and 0 <= dm < M:
                            if land[dn][dm] == 1 and (dn, dm) not in visit:
                                queue.append((dn, dm))

                result += 1

    print(result)