import sys
from itertools import combinations

N = int(sys.stdin.readline())
arr = [[0] * N for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, sys.stdin.readline().split()))

visited = [False for _ in range(N)]
result = 1000000000


def dfs(depth, idx):
    global result
    if depth == N//2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += (arr[i][j])
                elif not visited[i] and not visited[j]:
                    link += (arr[i][j])
        result = min(result, abs(start - link))

        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


dfs(0, 0)
print(result)
# people = [i for i in range(N)]
# teams = list(combinations(people, N//2))
# result = 1000000000
# for team in teams[:len(teams)//2]:
#     start = list(team)
#     link = list(set(people) - set(start))
#     skill_start = 0
#     skill_link = 0
#     couple_start = list(combinations(start, 2))
#     couple_link = list(combinations(link, 2))
#
#     for s, l in zip(couple_start, couple_link):
#         skill_start += arr[s[0]][s[1]] + arr[s[1]][s[0]]
#         skill_link += arr[l[0]][l[1]] + arr[l[1]][l[0]]
#         sub = abs(skill_start - skill_link)
#
#     result = min(result, abs(skill_start - skill_link))
#
# print(result)
