# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# 첫 번째 풀이 (시간 초과)
def solution(participant, completion):
    
    for p in participant:                                   # 이중 반복문
        for c in completion:
            if p == c:
                completion.remove(c)
                break
        else:
            return p

# 두 번째 풀이 (딕셔너리 활용)
from collections import Counter

def solution(participant, completion):
    
    p = Counter(participant)

    for c in completion:
        if c in p:                                          # 참가자가 완주했으면
            p[c] -= 1                                       # 참가자의 count - 1

    return [k for k, v in p.items() if v == 1][0]

'''
회고 / TIL
- 역시나 무턱대고 푸니 효율성에서 시간 초과 발생함.
- Counter를 이용해 계수 정렬처럼 풀었음.
'''