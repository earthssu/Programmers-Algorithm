import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sset = list(set(arr))
sset.sort()

dic = dict()
for i in range(len(sset)):
    dic[sset[i]] = i

for a in arr:
    print(dic[a], end=' ')