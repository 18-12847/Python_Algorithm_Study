def solution(num, k):
    stack = []
    for i in num:
        while stack and i > stack[-1] and k > 0:
            k -= 1
            stack.pop()
        stack.append(i)
    if k != 0:
        return "".join(stack[:-k])
    return "".join(stack)