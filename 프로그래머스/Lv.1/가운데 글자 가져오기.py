# https://school.programmers.co.kr/learn/courses/30/lessons/12903

# 나의 풀이
def solution(s):
    ls = len(s)
    
    if ls % 2:                                              # 길이가 홀수면
        return s[ls // 2]                                   # 몫 인덱스를 출력
    else:
        return s[(ls // 2) - 1:(ls // 2) + 1]               # 짝수면 몫 - 1과 몫 인덱스를 출력

# 다른 사람의 풀이
def string_middle(str):
    return str[(len(str) - 1) // 2:len(str) // 2 + 1]       # len(s)에 1을 빼서 짝수 / 홀수 상관없이 계산함.


'''
회고 / TIL
- 풀이 방식이 다양했지만, 짝수 홀수를 구분짓지 않는 방법이 신기했음.
'''