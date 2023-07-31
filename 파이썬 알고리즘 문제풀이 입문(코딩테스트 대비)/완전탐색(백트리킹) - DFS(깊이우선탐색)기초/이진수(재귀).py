import sys
input = sys.stdin.readline
def dfs(n):
    if n == 0:
        return
    else:
        dfs(n // 2)
        print(n % 2, end ="")
dfs(int(input().rstrip()))