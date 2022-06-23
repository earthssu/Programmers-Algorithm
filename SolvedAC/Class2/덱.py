import sys


N = int(sys.stdin.readline())
deque = []
result = []

for i in range(N):
    oper = sys.stdin.readline().strip()
    if 'push_front' in oper:
        num = int(oper.split(" ")[1])
        deque.insert(0, num)
    elif 'push_back' in oper:
        num = int(oper.split(" ")[1])
        deque.append(num)
    elif oper == 'pop_front':
        if len(deque):
            num = deque.pop(0)
            result.append(num)
        else:
            result.append(-1)
    elif oper == 'pop_back':
        if len(deque):
            num = deque.pop()
            result.append(num)
        else:
            result.append(-1)
    elif oper == 'size':
        result.append(len(deque))
    elif oper == 'empty':
        if len(deque):
            result.append(0)
        else:
            result.append(1)
    elif oper == 'front':
        if len(deque):
            result.append(deque[0])
        else:
            result.append(-1)
    else:
        if len(deque):
            result.append(deque[-1])
        else:
            result.append(-1)

for r in result:
    print(r)