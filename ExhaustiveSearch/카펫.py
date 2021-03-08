def solution(brown, yellow):
    for d in range(1, yellow+1):
        if yellow % d == 0:
            if (d+2)*(yellow // d + 2) == (brown + yellow):
                return [yellow // d + 2, d + 2]


def solution_other(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]