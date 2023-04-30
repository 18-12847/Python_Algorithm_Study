import heapq
#Min Heap만 사용 가능
#Heap 요소 추가
heap = []
heapq.heappush(heap, 45)
heapq.heappush(heap, 36)
heapq.heappush(heap, 54)
heapq.heappush(heap, 27)
heapq.heappush(heap, 63)
print(heap) #27, 36, 54, 45, 63

#Heap 요소 제거
print(heapq.heappop(heap)) #27
print(heapq.heappop(heap)) #36
print(heapq.heappop(heap)) #45

print(heap) #54 63
#Heap 요소 제거 후 추가
heapq.heapreplace(heap, 10)
print(heap) #10 63

#Heap 요소 추가 후 제거
heapq.heappushpop(heap, 5)
print(heap) #10 63