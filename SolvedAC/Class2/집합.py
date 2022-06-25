import sys


N = int(sys.stdin.readline())
S = 0b000000000
result = []
for i in range(N):
    oper = sys.stdin.readline().strip()
    if 'add' in oper:
        num = int(oper.split(" ")[1])
        S |= (1 << num)
    elif 'remove' in oper:
        num = int(oper.split(" ")[1])
        S &= ~(1 << num)
    elif 'check' in oper:
        num = int(oper.split(" ")[1])
        print(1 if S & (1 << num) != 0 else 0)
    elif 'toggle' in oper:
        num = int(oper.split(" ")[1])
        S ^= (1 << num)
    elif 'all' in oper:
        S = (1 << 21) - 1
    else:
        S = 0

for r in result:
    print(r)