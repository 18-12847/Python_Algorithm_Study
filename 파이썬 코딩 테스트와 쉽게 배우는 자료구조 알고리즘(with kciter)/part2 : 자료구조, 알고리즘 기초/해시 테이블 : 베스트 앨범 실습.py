def solution(genres, plays):
    dic, ans = {}, []
    for idx, val in enumerate(genres):
        if val not in dic:
            dic[val] = []
        dic[val].append(plays[idx])
    for i in dic:
        dic[i] = sorted(dic[i], reverse = True)        
    lst = sorted(dic.items(), key = lambda x: sum(x[1]), reverse = True)
    for i in lst:
        if len(i[1]) == 0:
            continue
        elif len(i[1]) == 1:
            ans.append(plays.index(i[1][0]))
        else:
            if i[1][0] == i[1][1]:
                tmp = [idx for idx, val in enumerate(plays) if val == i[1][0]]
                ans.append(tmp[0])
                ans.append(tmp[1])
            else:
                ans.append(plays.index(i[1][0]))
                ans.append(plays.index(i[1][1]))
    return ans