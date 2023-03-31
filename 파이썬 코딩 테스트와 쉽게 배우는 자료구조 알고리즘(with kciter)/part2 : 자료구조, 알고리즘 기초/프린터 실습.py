from collections import deque
def solution(priorities, location):
    queue = deque(priorities)
    queue[location] = float(queue[location])
    flag = type(float(queue[location]))
    cnt = 1
    while True:
        if type(queue[0]) == flag and queue[0] >= max(queue):
            queue.popleft()
            return cnt
        elif type(queue[0]) == flag and queue[0] < max(queue):
            queue.append(queue.popleft())
        elif type(queue[0]) != flag and queue[0] >= max(queue):
            queue.popleft()
            cnt += 1
        elif type(queue[0]) != flag and queue[0] < max(queue):
            queue.append(queue.popleft())