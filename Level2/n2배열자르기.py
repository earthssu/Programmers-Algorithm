def solution(n, left, right):
    answer = []
        
    for curr in range(left, right+1):
        if (curr % n) <= (curr // n):
            answer.append((curr // n) + 1)
        else:
            answer.append((curr % n) + 1)
        
    return answer
