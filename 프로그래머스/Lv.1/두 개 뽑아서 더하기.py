# https://school.programmers.co.kr/learn/courses/30/lessons/68644

# 나의 풀이
from itertools import combinations

def solution(numbers):
    answer = set()                                      # 중복을 허용하지 않기 위해 처음부터 set 선언

    for i in combinations(numbers, 2):                  # numbers에서 2개씩 조합
        answer.add(sum(i))                              # 조합의 합을 answer에 추가
    
    return sorted(answer)                               # 정렬해서 리턴

# 다른 사람의 풀이
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):                       # 2중 for문 활용
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    return sorted(list(set(answer)))                    # 마지막에 중복 제거

'''
회고 / TIL
- 이번에도 조합을 먼저 떠올렸고, 조합의 합을 처음부터 set에 add해 중복을 허용하지 않도록 풀었음.
- 다른 사람의 풀이보다 내 풀이가 조금 더 좋은 것 같음.
'''