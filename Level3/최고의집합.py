def solution(n, s):
    answer = []
    
    if s < n:
        return [-1]
    
    for _ in range(n):
        answer.append(s // n)
    
    idx = len(answer) - 1
    
    for i in range(s - sum(answer)):
        answer[idx] += 1
        idx -= 1
    
    return answer
