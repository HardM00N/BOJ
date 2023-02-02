# https://school.programmers.co.kr/learn/courses/30/lessons/12977

# 나의 풀이
from itertools import combinations

def solution(nums):
    prime_cnt = 0

    for i in combinations(nums, 3):                     # 조합
        num = sum(i)

        for j in range(2, int(num ** 0.5) + 1):         # 소수 판별
            if num % j == 0:
                break
        else:
            prime_cnt += 1

    return prime_cnt

'''
회고 / TIL
- 다들 고만고만한 풀이로 비슷함.
'''