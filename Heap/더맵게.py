import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1

        answer += 1
        fir = heapq.heappop(scoville)
        sec = heapq.heappop(scoville)
        heapq.heappush(scoville, fir + (sec*2))

    return answer
