import sys

N = int(sys.stdin.readline())
tree = dict()
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    if a not in tree.keys():
        tree[a] = [b]
    else:
        tree[a].append(b)
    if b not in tree.keys():
        tree[b] = [a]
    else:
        tree[b].append(a)

result = [0] * (N+1)
visited = [False] * (N+1)
stack = [1]

while stack:
    node = stack.pop()
    visited[node] = True
    child = tree[node]
    if child:
        for c in child:
            if not visited[c]:
                result[c] = node
                stack.append(c)

for r in result[2:]:
    print(r)