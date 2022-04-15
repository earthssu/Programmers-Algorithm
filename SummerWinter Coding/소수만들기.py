from itertools import combinations


def solution(nums):
    answer = 0

    combination = list(combinations(nums, 3))
    for com in combination:
        c_sum = sum(com)
        for i in range(2, c_sum):
            if c_sum % i == 0:
                break
        else:
            answer += 1

    return answer