from itertools import permutations

def solution(k, dungeons):
    answer = -1
    dun_list = list(permutations(dungeons, len(dungeons)))
    
    for dun in dun_list:
        tired = k
        cnt = 0
        for d in dun:
            if tired < d[0]:
                break
            else:
                tired -= d[1]
                cnt += 1
        answer = max(cnt, answer)

    return answer
