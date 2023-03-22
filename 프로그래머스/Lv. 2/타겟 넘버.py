# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# 나의 풀이
cnt = 0

def solution(numbers, target):
    def dfs(tmp, depth):
        global cnt
        
        if depth == len(numbers):                       # 재귀의 끝에 도달했을 때
            if tmp == target:                           # 합이 target이라면 카운트
                cnt += 1
            return
        
        dfs(tmp + numbers[depth], depth + 1)            # 재귀의 끝에 도달할 때까지 호출
        dfs(tmp - numbers[depth], depth + 1)
    
    dfs(0, 0)
    return cnt

# 다른 사람의 풀이
from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))                     # product() : 요소들의 모든 조합을 구함
    
    return s.count(target)

'''
회고 / TIL
- 그래프 오랜만이라 이코테 다시 보고 풀었음. 
- 문제 자체보다 cnt 변수 scope 처리를 잘못해서 애먹음. 
- 다른 사람의 product를 이용한 편리한 풀이에 진심으로 감탄함.
'''