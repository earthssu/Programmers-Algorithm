from collections import deque


N, K = map(int, input().split())
MAX = 10 ** 5
dist = [0] * (MAX + 1)

queue = deque([N])
while True:
    loc = queue.popleft()
    if loc == K:
        print(dist[loc])
        break

    for nx in (loc-1, loc+1, 2*loc):
        if 0 <= nx <= MAX and not dist[nx]:
            dist[nx] = dist[loc] + 1
            queue.append(nx)