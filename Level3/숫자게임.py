def solution(A, B):
    answer = 0
    size = len(A)
    idx = 0
    chk_idx = 0
    
    A.sort()
    B.sort()

    while idx < size:
        if chk_idx == size:
            break
            
        if A[idx] < B[chk_idx]:
            answer += 1
            idx += 1
        
        chk_idx += 1

    return answer
