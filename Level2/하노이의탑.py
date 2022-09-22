answer = []


def hanoi(n, from_pos, to_pos, mid_pos):
    if n == 1:
        answer.append([from_pos, to_pos])
        return

    hanoi(n-1, from_pos, mid_pos, to_pos)
    answer.append([from_pos, to_pos])
    hanoi(n-1, mid_pos, to_pos, from_pos)


def solution(n):
    hanoi(n, 1, 3, 2)
    return answer