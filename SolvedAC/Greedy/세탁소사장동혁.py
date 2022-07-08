import sys


M = int(sys.stdin.readline())

for _ in range(M):
    money = [[25, 0], [10, 0], [5, 0], [1, 0]]
    change = int(sys.stdin.readline())
    idx = 0
    while change > 0:
        money[idx][1], change = divmod(change, money[idx][0])
        idx += 1
    for m in money:
        print(m[1], end=' ')
    print()