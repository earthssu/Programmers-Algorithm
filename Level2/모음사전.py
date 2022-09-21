from itertools import product


def solution(word):
    answer = 0
    alpha = ["A", "E", "I", "O", "U"]
    dictionary = []

    for i in range(1, 6):
        pro = list(product(alpha, repeat=i))
        for p in pro:
            dictionary.append(''.join(p))

    dictionary.sort()

    return dictionary.index(word) + 1