import sys


N = int(sys.stdin.readline())
stack = []
result = []

for i in range(N):
    oper = sys.stdin.readline().strip()
    if 'push' in oper:
        num = int(oper.split(" ")[1])
        stack.append(num)
    elif oper == 'pop':
        if len(stack) > 0:
            num = stack.pop()
            result.append(num)
        else:
            result.append(-1)
    elif oper == 'size':
        result.append(len(stack))
    elif oper == 'empty':
        if len(stack) > 0:
            result.append(0)
        else:
            result.append(1)
    else:
        if len(stack) > 0:
            result.append(stack[-1])
        else:
            result.append(-1)

for r in result:
    print(r)
