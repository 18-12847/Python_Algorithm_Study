import heapq
def solution(no, works):
    heap = []
    for i in works:
        heapq.heappush(heap, -i)
    for i in range(no):
        # heapq.heappush(heap, heapq.heappop(heap) + 1)
        heapq.heapreplace(heap, heap[0] + 1)
    tot = 0
    for i in heap:
        tot += i ** 2
    return tot if sum(works) > no else 0