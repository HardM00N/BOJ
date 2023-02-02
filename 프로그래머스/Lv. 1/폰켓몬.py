# https://school.programmers.co.kr/learn/courses/30/lessons/1845

# 나의 풀이
def solution(nums):
    N = len(nums) // 2
    nums = set(nums)                            # 중복 제거

    if N < len(nums):
            return N
    else:
        return len(nums)

# 다른 사람의 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))         # min 활용

'''
회고 / TIL
- 중복만 제거하면 쉽게 풀리는 문제였음.
'''