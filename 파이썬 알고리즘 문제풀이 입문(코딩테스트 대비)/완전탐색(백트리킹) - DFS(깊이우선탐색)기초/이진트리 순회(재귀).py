import sys
input = sys.stdin.readline
def dfs(v):
    if v > 7:
        return
    else:
        print(v, end = " ") # 전위
        dfs(v * 2)
        print(v, end = " ") # 중위
        dfs(v * 2 + 1)
        print(v, end = " ") # 후위 
dfs(1)