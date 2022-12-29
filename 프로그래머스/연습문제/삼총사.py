# https://school.programmers.co.kr/learn/courses/30/lessons/131705

# 나의 풀이
from itertools import combinations

def solution(number):
    cnt = 0
    
    for i in combinations(number, 3):                           # 3개씩 조합
        if sum(i) == 0:                                         # 조합의 합이 0이면
            cnt += 1                                            # 삼총사 카운트
    
    return cnt

# 다른 사람의 풀이
def solution(number):
    answer = 0
    l = len(number)
    for i in range(l - 2):
        for j in range(i + 1, l - 1):
            for k in range(j + 1, l):
                if number[i] + number[j] + number[k] == 0:      # 3중 for문 활용
                    answer += 1           
    return answer

'''
회고 / TIL
- 문제를 보자마자 합이 0이 되는 조합을 찾아야할 것 같아서 itertools의 combinations를 사용함.
- 다른 사람의 풀이와 완전히 같아서 신기했음.
'''