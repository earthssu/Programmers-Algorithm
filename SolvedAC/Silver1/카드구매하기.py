import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

money = [0] * (N+1)
money[1] = cards[0]
for i in range(2, N+1):
    for j in range(1, N+1):
        money[i] = max(money[j]+money[i-j], cards[i-1], money[i])

print(money[-1])
