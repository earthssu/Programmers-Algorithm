from collections import defaultdict

cases = []


def dfs(banned_dict, i, case=[]):
    if i == len(banned_dict):
        cases.append(case)
        return
    for j in range(len(banned_dict[i])):
        if banned_dict[i][j] not in case:
            case.append(banned_dict[i][j])
            dfs(banned_dict, i+1, case[:])
            case.pop()


def solution(user_id, banned_id):
    banned_dict = defaultdict(list)
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            if len(banned_id[i]) == len(user_id[j]):
                flag = True
                for k in range(len(banned_id[i])):
                    if banned_id[i][k] != user_id[j][k] and banned_id[i][k] != '*':
                        flag = False
                        break
                if flag:
                    banned_dict[i].append(j)
    global cases
    dfs(banned_dict, 0)
    answer = len(set([tuple(sorted(case)) for case in cases]))
    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))