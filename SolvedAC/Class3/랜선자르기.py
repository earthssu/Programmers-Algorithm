import sys

K, N = map(int, sys.stdin.readline().split())
lans = []
for _ in range(K):
    num = int(sys.stdin.readline())
    lans.append(num)

end = max(lans)
start = 1
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for l in lans:
        cnt += (l // mid)

    if cnt < N:
        end = mid - 1
    elif cnt >= N:
        start = mid + 1

print(end)