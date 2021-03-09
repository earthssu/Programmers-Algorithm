import heapq


def solution(operations):
    heap = []
    while operations:
        opr, num = operations.pop(0).split(" ")
        if opr == "I":
            heapq.heappush(heap, int(num))
        else:
            if heap:
                if num == "-1":
                    heapq.heapify(heap)
                    heapq.heappop(heap)
                else:
                    heap = [-x for x in heap]
                    heapq.heapify(heap)
                    heapq.heappop(heap)
                    heap = [-x for x in heap]

    if heap:
        answer = [max(heap), min(heap)]
    else:
        answer = [0, 0]
    return answer


def solution_other(arguments):
    max_heap = []
    min_heap = []
    for arg in arguments:
        if arg == "D 1":
            if max_heap != []:
                heapq.heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif arg == "D -1":
            if min_heap != []:
                heapq.heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:
            num = int(arg[2:])
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
    if min_heap == []:
        return [0, 0]
    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
