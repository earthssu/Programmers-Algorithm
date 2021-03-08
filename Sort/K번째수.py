def solution(array, commands):
    answer = []
    for com in commands:
        i, j, k = com
        answer.append(sorted(array[i-1:j])[k-1])
    return answer