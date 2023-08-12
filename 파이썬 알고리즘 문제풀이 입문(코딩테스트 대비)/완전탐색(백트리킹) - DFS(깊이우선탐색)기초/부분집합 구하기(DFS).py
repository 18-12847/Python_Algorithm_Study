import sys
input = sys.stdin.readline
def dfs(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if check[i]:
                print(i, end = " ")
        print()
    else:
        check[v] = 1
        dfs(v + 1)
        check[v] = 0
        dfs(v + 1)
        
n = int(input().rstrip())
check = [0] * (n + 1)
dfs(1)