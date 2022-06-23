import sys


N = int(sys.stdin.readline())
queue = []
result = []

for i in range(N):
    oper = sys.stdin.readline().strip()
    if 'push' in oper:
        num = int(oper.split(" ")[1])
        queue.append(num)
    elif oper == 'pop':
        if len(queue):
            num = queue.pop(0)
            result.append(num)
        else:
            result.append(-1)
    elif oper == 'size':
        result.append(len(queue))
    elif oper == 'empty':
        if len(queue):
            result.append(0)
        else:
            result.append(1)
    elif oper == 'front':
        if len(queue):
            result.append(queue[0])
        else:
            result.append(-1)
    else:
        if len(queue):
            result.append(queue[-1])
        else:
            result.append(-1)

for r in result:
    print(r)