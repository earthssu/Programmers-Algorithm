from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []

    for num in course:
        order_dict = defaultdict(int)
        for order in orders:
            order = sorted(list(order))
            for c in combinations(order, num):
                tmp_c = ''.join(c)
                order_dict[tmp_c] += 1
        max_num = 0
        for menu in order_dict:
            if order_dict[menu] > max_num:
                max_num = order_dict[menu]

        for menu in order_dict:
            if order_dict[menu] == max_num and max_num > 1:
                answer.append(menu)

    answer = sorted(answer)
    return answer