# https://school.programmers.co.kr/learn/courses/30/lessons/87946

# 나의 풀이
from itertools import permutations

def solution(k, dungeons):    
    p_list = permutations(dungeons, len(dungeons))      # 던전의 모든 순열 생성
    res = 0

    for p in p_list:                                    # 순열들 중에서 하나씩 가져와서
        hp = k
        
        for idx, i in enumerate(p):                     # 가져온 순열 내의 던전을 하나씩 돌며
            if i[0] > hp:                               # hp보다 소모 피로도가 크다면 던전 개수 카운트 후 종료
                res = max(res, idx)
                break
            else:                                       # hp가 소모 피로도보다 더 크다면 계속 던전 돌기
                hp -= i[1]
        else:
            return len(dungeons)                        # for문이 다 돌았다 -> 모든 던전을 돌았으므로 던전의 길이 리턴
    
    return res                                          # 모든 던전을 다 돌지 못한 경우에도 최대로 돈 던전 개수 리턴

# 다른 사람의 풀이 (틀렸지만 접근이 좋은 풀이, 효율성으로 정렬)
def solution(k, dungeons):
    answer = 0
    dungeons = sorted(dungeons, key=lambda x: ((x[1] + x[0]) / x[0], x[1]))
    
    for x, y in dungeons:
        if k >= x:
            k -= y
            answer += 1
    
    return answer

'''
회고 / TIL
- 무식하게 순열로 때려박았는데 완전탐색 문제라 그런가 잘 돌아갔음.
- 풀이법이 겁나 다양함.
'''