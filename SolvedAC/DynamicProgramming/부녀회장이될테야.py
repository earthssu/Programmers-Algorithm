import sys
T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    apt = [[0]*(n+1) for _ in range(k+1)]

    for i in range(1, n+1):
        apt[0][i] = i

    for i in range(1, k+1):
        for j in range(1, n+1):
            apt[i][j] = apt[i-1][j] + apt[i][j-1]

    print(apt[k][n])
