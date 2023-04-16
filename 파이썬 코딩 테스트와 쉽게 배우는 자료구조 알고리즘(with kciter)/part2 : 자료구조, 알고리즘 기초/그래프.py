#인접행렬
graph = [[False] * 5 for _ in range(5)]
graph[0][1] = True #0 -> 1
graph[0][3] = True #0 -> 3
graph[1][2] = True #1 -> 2
graph[2][0] = True #2 -> 0
graph[2][4] = True #2 -> 4
graph[3][2] = True #3 -> 2
graph[4][0] = True #4 -> 0

#연결리스트 그래프
graph = [[] * 5 for _ in range(5)]
graph[0].append(1) #0 -> 1
graph[0].append(3) #0 -> 3
graph[1].append(2) #1 -> 2
graph[2].append(0) #2 -> 0
graph[2].append(4) #2 -> 4
graph[3].append(2) #3 -> 2
graph[4].append(0) #4 -> 0