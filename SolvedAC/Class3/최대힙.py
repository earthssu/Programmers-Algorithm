import heapq
import sys


heap = []
heapq.heapify(heap)
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 0:
        heapq.heappush(heap, -num)
    elif num == 0:
        if heap:
            p = heapq.heappop(heap)
            print(-p)
        else:
            print(0)