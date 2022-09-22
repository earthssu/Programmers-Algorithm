import math

def solution(n, a, b):
    answer = 1

    while True:
        if abs(b - a) == 1:
            min_num = min(a, b)
            if a == min_num:
                if a % 2 == 1:
                    break
            else:
                if b % 2 == 1:
                    break

        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        answer += 1

    return answer


def solution_other(n, a, b):
    answer = 0
    while a != b:
        answer += 1
        a = (a+1)//2
        b = (b+1)//2
    return answer