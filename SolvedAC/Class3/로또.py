import sys
from itertools import combinations

while True:
    arr = list(map(int, sys.stdin.readline().split()))
    if arr[0] == 0:
        break
    N = arr[0]
    lotto = arr[1:]
    results = list(combinations(lotto, 6))
    for result in results:
        for r in result:
            print(r, end=' ')
        print()
    print()