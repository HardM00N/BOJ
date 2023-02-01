# https://school.programmers.co.kr/learn/courses/30/lessons/12932

# 나의 풀이
def solution(n):
    array = list(str(n))
    array.reverse()
    return list(map(int, array))

# 다른 사람의 풀이
def digit_reverse(n):
    return list(map(int, reversed(str(n))))     # 더 짧고 간결하게 푸심... reversed...

'''
회고 / TIL
- 간단한 문제지만, 다양한 풀이법이 있어서 스킬을 익히기 좋았음. 
'''