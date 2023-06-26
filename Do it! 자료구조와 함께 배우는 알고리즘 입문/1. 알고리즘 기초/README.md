<pre>
def med3(a, b, c):
    if (b >= a and c <= a) or (b <= a and c>= a):
        return a
    elif (b >= a and c <= a) or (b <= a and c>= a):
        return b
    return c
</pre>
- 비교해야 할 조건이나 비교가 많아질 수도 있어서 코드가 짧다고 좋은게 아니다.
<pre>
def med3(a, b, c):
    if a>= b:
        if b>= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b
</pre>
- 가우스 덧셈으로 1부터 n까지 정수의 합 구하기 : n * (n + 1) / 2
