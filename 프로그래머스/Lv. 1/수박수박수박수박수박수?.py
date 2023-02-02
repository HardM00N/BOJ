# https://school.programmers.co.kr/learn/courses/30/lessons/12922

# 나의 풀이
def solution(n):
    answer = ''
    
    for i in range(n):
        if (i + 1) % 2:         # 홀수번째 자리
            answer += '수'
        else:                   # 짝수번째 자리
            answer += '박'

    return answer

# 다른 사람의 풀이
def water_melon(n):
    return "수박" * (n // 2) + "수" * (n % 2)   # 짝수만큼 수박을 반복, 홀수라면 수를 더함

'''
회고 / TIL
- 대체로 풀이가 비슷하지만, 좀 더 쉽게도 풀 수 있었음.
'''