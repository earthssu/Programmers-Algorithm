def solution(s):
    idx = 1
    s = list(s)
    stack = []

    for i in range(len(s)):
        if s[i] in stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    if len(stack) > 0:
        return 0
    else:
        return 1