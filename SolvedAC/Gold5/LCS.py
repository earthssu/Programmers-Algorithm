import sys

seq_a = list(sys.stdin.readline().rstrip())
seq_b = list(sys.stdin.readline().rstrip())
l1, l2 = len(seq_a), len(seq_b)
cache = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < cache[j]:
            cnt = cache[j]
        elif seq_a[i] == seq_b[j]:
            cache[j] = cnt + 1

print(max(cache))