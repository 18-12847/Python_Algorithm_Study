import sys
input = sys.stdin.readline
def dfs(lst_index, tot_sum):
    if tot_sum > tot // 2:
        return
    if lst_index == n:
        if tot_sum == tot - tot_sum:
            print("YES")
            sys.exit(0)
    else:
        dfs(lst_index + 1, tot_sum + lst[lst_index])
        dfs(lst_index + 1, tot_sum)
    
n = int(input().rstrip())
lst = list(map(int, input().split()))
tot = sum(lst)
dfs(0, 0)
print("NO")