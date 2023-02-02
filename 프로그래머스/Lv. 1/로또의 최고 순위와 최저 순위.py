# https://school.programmers.co.kr/learn/courses/30/lessons/77484

# 나의 예전 풀이
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    
    zeros = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            cnt += 1
    
    return rank[cnt+zeros], rank[cnt]

# 나의 현재 풀이
def solution(lottos, win_nums):
    
    cnt, zero_cnt = 0, 0
    win_nums = set(win_nums)
    
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
        if lotto == 0:
            zero_cnt += 1
    
    result = [6, 6, 5, 4, 3, 2, 1]

    return [result[cnt + zero_cnt], result[cnt]]

# 다른 사람의 풀이
def solution(lottos, win_nums):
    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]

'''
회고 / TIL
- 전에 풀었던 문제라 쉽게 풀었음.
- set의 교집합을 이용한 다른 사람의 풀이... 크...
'''