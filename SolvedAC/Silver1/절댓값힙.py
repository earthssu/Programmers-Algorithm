import sys
import heapq

N = int(sys.stdin.readline())
heap = []
heapq.heapify(heap)

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        num_abs = abs(num)
        if num_abs != num:
            num_abs -= 0.5
        heapq.heappush(heap, (num_abs, num))
