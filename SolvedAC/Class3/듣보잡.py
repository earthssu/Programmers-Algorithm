import sys


N, M = map(int, sys.stdin.readline().split(" "))
hear = []
see = []
for i in range(N):
    hear.append(sys.stdin.readline().strip())
for j in range(M):
    see.append(sys.stdin.readline().strip())

result = sorted(list(set(hear) & set(see)))
print(len(result))
for r in result:
    print(r)