N = int(input())
result = []
for i in range(N):
    bracket = list(input())
    stack = []
    flag = True
    for b in bracket:
        if b == '(':
            stack.append(b)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                flag = False
                break

    if len(stack) == 0 and flag == True:
        result.append('YES')
    elif len(stack) != 0 or flag == False:
        result.append('NO')

for r in result:
    print(r)
