from itertools import combinations as combi
from collections import defaultdict


def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    for i in info:
        i = i.split()
        i_key = i[:-1]
        i_val = int(i[-1])
        for k in range(5):
            for c in combi(i_key, k):
                tmp_c = ''.join(c)
                info_dict[tmp_c].append(i_val)

    for key in info_dict.keys():
        info_dict[key].sort()

    for q in query:
        q = q.split(' ')
        q_score = int(q[-1])
        q = q[:-1]

        for r in range(3):
            q.remove('and')
        while '-' in q:
            q.remove('-')
        tmp_q = ''.join(q)

        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= q_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:
            answer.append(0)

    return answer