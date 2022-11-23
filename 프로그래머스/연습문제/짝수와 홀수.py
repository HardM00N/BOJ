# https://school.programmers.co.kr/learn/courses/30/lessons/12937

# 나의 풀이
def solution(num):
    
    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    
    return answer

# 다른 사람의 풀이
def evenOrOdd(num):
    return ["Even", "Odd"][num & 1]     # 1과 비트 연산해 0이면 짝수, 1이면 홀수

'''
회고 / TIL
- 오랜만에 푸는 기본 문제라 풀이 자체에 어려움은 없었음. 
- 다만 비트 연산자를 활용한 천상계 풀이에 입을 다물지 못함...
'''