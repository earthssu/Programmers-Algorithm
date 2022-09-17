import sys

N, K = map(int, sys.stdin.readline().split())
weight = []
value = []
for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    weight.append(w)
    value.append(v)


def knapsack(capacity, n):
    array = [[0] * (capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for s in range(1, capacity+1):
            if weight[i-1] > s:
                array[i][s] = array[i-1][s]
            else:
                array[i][s] = max(array[i-1][s], value[i-1]+array[i-1][s-weight[i-1]])
    return array[n][capacity]


print(knapsack(K, N))