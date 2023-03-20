# https://school.programmers.co.kr/learn/courses/30/lessons/138476

# 나의 풀이
from collections import Counter

def solution(k, tangerine):
    res = 0

    for c in Counter(tangerine).most_common():          # 최빈값부터 정렬
        k -= c[1]
        res += 1

        if k <= 0:
            break
    
    return res

# 다른 사람의 풀이
from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    tangerine.sort(key = lambda t: (-counter[t], t))    # lambda를 이용한 내림차순 정렬
    
    return len(set(tangerine[:k]))                      # set로 종류 개수 확인 [3, 3, 3, 1, 1, 1] -> [3, 1]

'''
회고 / TIL
- 각 요소의 개수를 내림차순 정렬한 뒤, k개만큼 취하면서 카운트하면 되는 문제임. 
- 다른 사람 풀이에서 set로 쉽게 종류를 구한 부분이 인상적임.
'''