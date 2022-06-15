from collections import deque


N = int(input())
arr = deque([i for i in range(1, N+1)])

flag = 1
while True:
    if len(arr) == 1:
        print(arr[0])
        break

    if flag == 1:
        arr.popleft()
        flag += 1
    else:
        a = arr.popleft()
        arr.append(a)
        flag = 1