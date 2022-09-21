def dfs(trees, start, n):
    global answer
    stack = [start]
    visited = [False] * (n+1)
    count = 1
    
    while stack:
        node = stack.pop()
        visited[node] = True
        if len(trees[node]) > 0:
            for t in trees[node]:
                if not visited[t]:
                    stack.append(t)
                    visited[t] = True
                    count += 1
                    
    return abs(count - (n - count))

def solution(n, wires):
    answer = n
    trees = [[] for _ in range(n+1)]
    s = 0
    for i in range(len(wires)+1):
        for j in range(len(wires)):
            if i != j:
                s = wires[j][0]
                trees[wires[j][0]].append(wires[j][1])
                trees[wires[j][1]].append(wires[j][0])
        result = dfs(trees, s, n)
        answer = min(answer, result)
        trees = [[] for _ in range(n+1)]  

    return answer
