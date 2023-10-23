import heapq
INF = 1000000000

def dijkstra(graph, n, start):
    heap = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        c_dist, c_node = heapq.heappop(heap)
        if distance[c_node] < c_dist:
            continue
        for n_node, n_dist in graph[c_node]:
            cost = c_dist + n_dist
            if distance[n_node] > cost:
                distance[n_node] = cost
                heapq.heappush(heap, (cost, n_node))
    return distance

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    cnt = 0
    for i in dijkstra(graph, N, 1):
        if i <= K:
            cnt += 1
    return cnt