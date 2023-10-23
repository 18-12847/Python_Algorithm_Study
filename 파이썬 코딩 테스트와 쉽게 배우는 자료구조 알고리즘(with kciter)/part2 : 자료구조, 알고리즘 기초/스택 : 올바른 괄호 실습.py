def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0 and i == ")":
            return False
        elif len(stack) == 0:
            stack.append(i)
        elif i == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(i)
    return False if len(stack) else True