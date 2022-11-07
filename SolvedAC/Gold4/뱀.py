from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

N = int(input())
town = [[0] * (N) for _ in range(N)]
apple = [[0] * (N) for _ in range(N)]
K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    apple[a-1][b-1] = 1
L = int(input())
dir_queue = deque([])
for _ in range(L):
    x, c = input().split()
    dir_queue.append((int(x), c))

r, c = 0, 0
queue = deque([(r, c)])
town[r][c] = 1
d = 2  # 방향
result = 0 # 경과 초
sec, dirc = dir_queue.popleft()  # 첫 번째 방향 전환
while True:
    nr = r + dx[d]
    nc = c + dy[d]
    result += 1
    if 0 <= nr < N and 0 <= nc < N and town[nr][nc] != 1:  # 다음 위치가 벽이 아니고 자기 몸도 아님
        r, c = nr, nc
        town[nr][nc] = 1
        if apple[nr][nc] == 1:
            apple[nr][nc] = 0
            queue.append((nr, nc))
        elif apple[nr][nc] == 0:
            queue.append((nr, nc))
            qr, qc = queue.popleft()
            town[qr][qc] = 0
    else:  # 부딪혔다면
        print(result)
        break
    # 방향 전환
    if result == sec:
        if dirc == 'L':
            d = (d-1) % 4
        else:
            d = (d+1) % 4
        if dir_queue:
            sec, dirc = dir_queue.popleft()
