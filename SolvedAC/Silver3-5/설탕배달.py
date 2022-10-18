import sys

N = int(sys.stdin.readline())
answer = 0

while N >= 0:
    if N % 5 == 0:
        answer += N // 5
        print(answer)
        break
    N -= 3
    answer += 1
else:
    print(-1)
