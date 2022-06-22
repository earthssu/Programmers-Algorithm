import sys


N = int(sys.stdin.readline())
have = list(map(int, sys.stdin.readline().split(" ")))
M = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split(" ")))

have_dict = {}
for h in have:
    if h not in have_dict.keys():
        have_dict[h] = 1
    else:
        have_dict[h] += 1

result = []
for f in find:
    if f in have_dict.keys():
        result.append(have_dict[f])
    else:
        result.append(0)

for r in result:
    print(r, end=' ')