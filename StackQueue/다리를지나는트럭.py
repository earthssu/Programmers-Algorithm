def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0] * bridge_length
    sq = 0
    while q:
        answer += 1
        temp1 = q.pop(0)

        if temp1 != 0:
            sq -= temp1

        if truck_weights:
            if sq + truck_weights[0] <= weight:
                temp2 = truck_weights.pop(0)
                q.append(temp2)
                sq += temp2
            else:
                q.append(0)

    return answer