from collections import deque


M = int(input())  # 컴퓨터의 수
N = int(input())  # 컴퓨터 쌍의 수

virus = dict()
for i in range(N):
    a, b = map(int, input().split())
    if a not in virus.keys():
        virus[a] = [b]
    else:
        virus[a].append(b)
    if b not in virus.keys():
        virus[b] = [a]
    else:
        virus[b].append(a)

visit = []
queue = deque([1])
while queue:
    node = queue.popleft()
    if node not in visit:
        visit.append(node)
        queue.extend(virus[node])

print(len(visit) - 1)