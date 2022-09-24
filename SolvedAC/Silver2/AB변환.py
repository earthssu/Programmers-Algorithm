from collections import deque

A, B = map(int, input().split())
queue = deque([(A, 1)])
flag = False
while queue:
    node = queue.popleft()
    case_a = node[0] * 2
    case_b = node[0] * 10 + 1
    if case_a == B or case_b == B:
        flag = True
        print(node[1]+1)
        break
    if case_a < B:
        queue.append((case_a, node[1]+1))
    if case_b < B:
        queue.append((case_b, node[1]+1))

if not flag:
    print(-1)
