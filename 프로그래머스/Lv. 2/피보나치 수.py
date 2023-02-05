# https://school.programmers.co.kr/learn/courses/30/lessons/12945

# 나의 풀이 (Top-Down, 재귀 + 메모이제이션)
import sys
sys.setrecursionlimit(10 ** 6)

def solution(n):
    dp = [0] * (n + 1)                                  # dp 테이블 초기화
    dp[1] = 1

    def fibo(x):                                        # 피보나치 함수
        if x < 2:
            return dp[x]

        if dp[x]:                                       # 이미 dp[x]가 존재한다면 바로 리턴
            return dp[x]
        else:
            dp[x] = fibo(x - 1) + fibo(x - 2)
            return dp[x]

    return fibo(n) % 1234567

# 다른 사람의 풀이 (Bottom-Up, 반복문으로 변수 두 개만 사용)
def solution(n):
    a, b = 0, 1
    
    for i in range(n):
        a, b = b, a + b
    
    return a % 1234567

'''
회고 / TIL
- 피보나치 문제는 항상 재귀 + 메모이제이션으로 풀게되는 것 같음.
- 반복적으로 푸는 연습을 하자.
'''