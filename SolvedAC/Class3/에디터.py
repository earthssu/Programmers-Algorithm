import sys

cursor_l = list(sys.stdin.readline().strip())
cursor_r = []
N = int(sys.stdin.readline())
for _ in range(N):
    oper = sys.stdin.readline().strip()
    if oper == 'L':
        if cursor_l:
            m = cursor_l.pop()
            cursor_r.append(m)
    elif oper == 'D':
        if cursor_r:
            m = cursor_r.pop()
            cursor_l.append(m)
    elif oper == 'B':
        if cursor_l:
            cursor_l.pop()
    else:
        char = oper.split()[1]
        cursor_l.append(char)

for l in cursor_l:
    print(l, end='')
for r in range(len(cursor_r)-1, -1, -1):
    print(cursor_r[r], end='')
