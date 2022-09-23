def knapsack(W, wt, val, n):
    K = [[0]*(W+1) for _ in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if n == 0 or W == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]


wt = []
val = []
N, K = map(int, input().split())
for i in range(N):
    w, v = map(int, input().split())
    wt.append(w)
    val.append(v)