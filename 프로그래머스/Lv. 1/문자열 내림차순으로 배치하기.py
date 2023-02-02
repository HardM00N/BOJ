# https://school.programmers.co.kr/learn/courses/30/lessons/12917

# 나의 풀이
def solution(s):
    ord_list = sorted([int(ord(x)) for x in s], reverse=True)       # 아스키코드 변환 후 정렬
    return ''.join([chr(x) for x in ord_list])                      # 다시 문자로 변환 후 반환

# 다른 사람의 풀이
def solution(s):
    return ''.join(sorted(s, reverse=True))                         # 아스키코드로 안 바꿔도 정렬이 됨...

'''
회고 / TIL
- 아스키코드로 변환해서 정렬하고 다시 문자열로 바꿨는데... 그냥 문자열 그대로 정렬해도 됨...
'''