import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

# 이분 탐색
start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for t in trees:
        if t > mid:
            total += t - mid
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)