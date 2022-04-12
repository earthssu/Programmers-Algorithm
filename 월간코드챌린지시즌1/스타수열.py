from collections import Counter


def solution(a):
    elements = Counter(a)
    answer = -1

    for k in elements.keys():
        if elements[k] <= answer:
            continue

        cnt = 0
        idx = 0
        while idx < len(a)-1:
            if (a[idx] != k and a[idx+1] != k) or (a[idx] == a[idx+1]):
                idx += 1
                continue
            cnt += 1
            idx += 2

        answer = max(answer, cnt)

    if answer == -1:
        return 0
    else:
        return answer * 2


print(solution([5,2,3,3,5,3]))