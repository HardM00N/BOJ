def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    
    zeros = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            cnt += 1
    
    return rank[cnt+zeros], rank[cnt]