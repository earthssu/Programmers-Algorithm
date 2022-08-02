import sys

N = int(sys.stdin.readline())
arr = [i for i in range(N+1)]

# 최소 개수가 꼭 큰 수의 제곱수로만 나타내는 것은 아님
for i in range(1, N+1):
    for j in range(1, i):
        if (j * j) > i:
            break
        else:
            if arr[i] > arr[i - j*j] + 1:
                arr[i] = arr[i - j*j] + 1

print(arr[N])