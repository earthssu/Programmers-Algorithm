def solution(name):
    cnt = [min(26 - ord(i) + 65, ord(i) - 65) for i in name if i != 'A']
    idx = [i for i, v in enumerate(name) if v != 'A']

    graph = [idx[i + 1] - idx[i] for i in range(len(idx) - 1)] + [len(name) - idx[-1]]
    if name[0] == 'A':
        idx = [0] + idx
        graph = [idx[1]] + graph

    answer = [2 * sum(graph[:i]) + (len(name) - idx[i + 1]) for i, v in enumerate(idx) if 0 < v < len(name) // 2] + [
        idx[-1], len(name) - idx[1]]
    return sum(cnt) + min(answer)

def solution_other(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer