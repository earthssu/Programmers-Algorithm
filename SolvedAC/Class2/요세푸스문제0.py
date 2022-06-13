from collections import deque


N, K = map(int, input().split(" "))
arr = deque([i for i in range(1, N+1)])
cnt = 1
result = []

while arr:
    num = arr.popleft()
    if cnt < K:
        arr.append(num)
        cnt += 1
    elif cnt == K:
        result.append(num)
        cnt = 1

print("<", end='')
for i in range(N):
    if i == N - 1:
        print(result[i], end='')
    else:
        print("{}, ".format(result[i]), end='')
print(">", end='')