def solution(tickets):
    routes = {}
    for t in tickets:
        if t[0] in routes:
            routes[t[0]].append(t[1])
        else:
            routes[t[0]] = [t[1]]

    for k in routes.keys():
        routes[k].sort(reverse=True)

    start = ["ICN"]
    answer = []
    while start:
        stack = start[-1]
        if stack not in routes or len(routes[stack]) == 0:
            answer.append(start.pop())
        else:
            start.append(routes[stack].pop())

    return answer[::-1]