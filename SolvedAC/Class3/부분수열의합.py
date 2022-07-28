import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
count = 0
for i in range(1, N+1):
    seq = list(combinations(arr, i))
    for s in seq:
        r = sum(list(s))
        if r == S:
            count += 1

print(count)