import heapq

def prim(graph, visited):
    heap, mst = [], 0
    heapq.heappush(heap, (0, 0))
    while heap:
        c_dist, c_node = heapq.heappop(heap)
        if visited[c_node]:
            continue
        visited[c_node] = 1
        mst += c_dist
        for n_node, n_dist in graph[c_node]:
            if visited[n_node]:
                continue
            heapq.heappush(heap, (n_dist, n_node))        
    return mst

def solution(n, costs):
    visited = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for a, b, c in costs:
        graph[a].append((b, c))
        graph[b].append((a, c))
    return prim(graph, visited)