# https://school.programmers.co.kr/learn/courses/30/lessons/12915

# 나의 풀이
def solution(strings, n):
    answer =  sorted(strings, key = lambda x: (x[n], x))    # x[n]을 기준으로 x들을 정렬
    return answer

'''
회고 / TIL
- 오랜만에 쉬운 문제...
- 다른 사람의 풀이랑 완전히 동일함.
'''