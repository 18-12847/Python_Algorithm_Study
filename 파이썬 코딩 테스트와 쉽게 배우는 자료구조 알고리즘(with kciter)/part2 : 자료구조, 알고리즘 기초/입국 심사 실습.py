def solution(n, t):
    left, right = t[0], t[-1] * n
    while left != right:
        mid = (left + right) // 2
        tmp = 0
        for i in t:
            tmp += mid // i
        if tmp < n:
            left = mid + 1
        else:
            right = mid
    return left
