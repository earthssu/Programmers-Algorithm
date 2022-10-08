string = input()
target = input()

stack = []

for s in string:
    stack.append(s)
    if s == target[-1] and ''.join(stack[-len(target):]) == target:
        del stack[-len(target):]

answer = ''.join(stack)
if len(answer) > 0:
    print(answer)
else:
    print("FRULA")