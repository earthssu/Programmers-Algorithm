import sys


N, M = map(int, sys.stdin.readline().split(" "))
arr = []
for n in range(N):
    a = list(sys.stdin.readline().strip())
    arr.append(a)

result = []
for a in range(N - 7):
    for b in range(M - 7):
        idx_w = 0
        idx_b = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if arr[i][j] != 'W':
                        idx_w += 1
                    else:
                        idx_b += 1
                elif (i+j) % 2 != 0:
                    if arr[i][j] != 'B':
                        idx_w += 1
                    else:
                        idx_b += 1

        result.append(min(idx_w, idx_b))

print(min(result))