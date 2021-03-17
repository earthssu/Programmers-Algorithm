import collections


def solution(participant, completion):
    answer = ''
    par_dic = {}
    for p in participant:
        if p in par_dic:
            par_dic[p] += 1
        else:
            par_dic[p] = 1
    for c in completion:
        par_dic[c] -= 1

    for pd in par_dic:
        if par_dic[pd] > 0:
            answer = pd
            break
    return answer


def solution_other(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


def solution_other2(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]