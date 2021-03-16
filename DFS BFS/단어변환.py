def dfs(begin, target, words, visited):
    answer = 0
    stacks = [begin]

    while stacks:
        stack = stacks.pop()
        if stack == target:
            return answer
        for w in range(len(words)):
            if len([i for i in range(len(words[w])) if words[w][i] != stack[i]]) == 1:
                if visited[w] != 0:
                    continue
                visited[w] = 1
                stacks.append(words[w])
        answer += 1


def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [0 for i in words]
    answer = dfs(begin, target, words, visited)
    return answer