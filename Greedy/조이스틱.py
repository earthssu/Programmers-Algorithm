def solution(name):
    cnt = [min(26 - ord(i) + 65, ord(i) - 65) for i in name if i != 'A']  # A 제외 알파벳별 최소 거리
    idx = [i for i, v in enumerate(name) if v != 'A']  # A 제외 알파벳별 위치
    graph = [idx[i + 1] - idx[i] for i in range(len(idx) - 1)] + [len(name) - idx[-1]]  # idx들 간의 거리 차

    # 맨 앞이 A일 경우에만 예외적으로 설정
    if name[0] == 'A':
        idx = [0] + idx  # idx 앞에 0 추가
        graph = [idx[1]] + graph  # graph 앞에 idx의 원래 첫 번째 요소였던 값 추가

    # [현재 위치에서 왼쪽, 오른쪽 이동한 경우의 합+남은 이동 거리 (단, 위치가 반 이상 넘어가지 않아야 함)]+[왼쪽으로만 이동, 오른쪽으로만 이동]
    answer = [2 * sum(graph[:i]) + (len(name) - idx[i + 1]) for i, v in enumerate(idx) if 0 < v < len(name) // 2] + \
             [idx[-1], len(name) - idx[1]]
    return sum(cnt) + min(answer)


def solution_other(name):
    answer = 0
    n = len(name)
    
    # 알파벳별 A까지의 최소 거리
    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    # 순수 이동 횟수
    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        # A가 있다면 계속 이동
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)  # 이동하는 방향에 따른 최솟값
        move = min(move, idx + n - next_idx + distance)  # min(순수 이동 횟수, 현재 위치+다음 알파벳 위치까지의 가야 할 거리+distance)

    answer += move
    return answer