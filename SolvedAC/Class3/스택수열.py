import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

curr = 2
idx = 0
stack = [1]
result = ['+']
flag = False
while True:
    if idx == N and len(stack) == 0:
        flag = True
        break

    if len(stack) and stack[-1] == arr[idx]:
        stack.pop()
        result.append('-')
        idx += 1
    else:
        if curr <= N:
            stack.append(curr)
            result.append("+")
            curr += 1
        else:
            break

if flag:
    for r in result:
        print(r)
else:
    print('NO')