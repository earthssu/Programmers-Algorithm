N, M = map(int, input().split())
S = dict()

for _ in range(N):
    ss = input()
    S[ss] = True

cnt = 0
for _ in range(M):
    ss = input()
    if ss in S:
        cnt += 1

print(cnt)
