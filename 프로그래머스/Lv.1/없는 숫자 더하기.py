# https://school.programmers.co.kr/learn/courses/30/lessons/86051

# 나의 풀이
def solution(numbers):
    mask = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    numbers = set(numbers)
    return sum(mask - numbers)                      # 차집합의 합

# 다른 사람의 풀이
def solution(numbers):
    return 45 - sum(numbers)                        # 단순히 전체 합에서 빼주기... 천재...

'''
회고 / TIL
- 나름 간편하게 풀었다 생각했지만 다른 사람의 풀이를 보니... 문제를 다각도로 생각하도록 노력해야겠음.
'''