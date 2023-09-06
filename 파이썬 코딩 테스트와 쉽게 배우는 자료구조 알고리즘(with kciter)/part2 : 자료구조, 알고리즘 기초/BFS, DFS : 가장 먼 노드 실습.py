from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for i in edge:
        a, b = i
        graph[a] += [b]
        graph[b] += [a]
    for i in range(1, n + 1):
        graph[i] = sorted(graph[i])

    visited = [0] * (n + 1)
    visited[1] = 1
    queue = deque([1])
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[cur] + 1
    return visited.count(max(visited))