import sys

N, M = map(int, sys.stdin.readline().split())
book_num = dict()
book_name = dict()
for n in range(1, N + 1):
    poke = sys.stdin.readline().strip()
    book_num[str(n)] = poke
    book_name[poke] = str(n)

for m in range(M):
    ans = sys.stdin.readline().strip()
    if ans in book_num.keys():
        print(book_num[ans])
    else:
        print(book_name[ans])
