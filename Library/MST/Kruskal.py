"""
신장트리에서 간선을 하나하나 더해가며 만드는 방식
신장트리
- 그래프에서 모든 정점에 대한 최소한의 연결만을 남긴 그래프
- N개의 정점을 가지는 그래프에 대해 N-1개의 간선 가짐
"""
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

node, edge = map(int, input().split())
parent = [0] * (node + 1)
edges = []
result = 0

for i in range(1, node+1):
    parent[i] = i

for _ in range(edge):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for ed in edges:
    cost, a, b = ed
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost