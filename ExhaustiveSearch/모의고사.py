def solution(answers):
    answer = []
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    result = [0] * 3
    for i in range(len(answers)):
        if answers[i] == student1[i % 5]:
            result[0] += 1
        if answers[i] == student2[i % 8]:
            result[1] += 1
        if answers[i] == student3[i % 10]:
            result[2] += 1

    m = max(result)
    for r in range(len(result)):
        if m == result[r]:
            answer.append(r+1)

    return answer

def solution_other(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]