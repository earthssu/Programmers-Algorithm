# 내 풀이
def solution(citations):
    citations.sort(reverse=True)
    answer = citations[0]

    while True:
        count_up = 0
        count_down = 0
        for temp in citations:
            if temp >= answer:
                count_up += 1
            else:
                count_down += 1
        if count_up >= answer >= count_down:
            break
        answer -= 1

    return answer

# 다른 풀이
def solution_other(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0