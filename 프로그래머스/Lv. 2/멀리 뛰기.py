# https://school.programmers.co.kr/learn/courses/30/lessons/12914

'''
1 -> (1) -> 1
2 -> (1, 1) (2) -> 2
3 -> (1, 1, 1) (1, 2) (2, 1) -> 3
4 -> (1, 1, 1, 1) (1, 1, 2) (1, 2, 1) (2, 1, 1) (2, 2) -> 5
5 -> (1, 1, 1, 1, 1) (1, 1, 1, 2) (1, 1, 2, 1) (1, 2, 1, 1) (2, 1, 1, 1) (1, 2, 2) (2, 1, 2) (2, 2, 1) -> 8

피보나치 수열임.
'''
# 나의 풀이 (재귀 & 메모이제이션)
import sys
sys.setrecursionlimit(10 ** 6)

def solution(n):
    dp = [0] * 2001
    dp[1] = 1
    dp[2] = 2

    def fibo(n):                                        # 피보나치 재귀 함수
        if n <= 2:
            return dp[n]
        if dp[n]:
            return dp[n]
        else:
            dp[n] = fibo(n - 1) + fibo(n - 2)           # 메모이제이션
            return dp[n]

    return fibo(n) % 1234567

# 다른 사람의 풀이
def jumpCase(num):
    a, b = 1, 2
    for i in range(2, num):                             # 반복적 피보나치
        a, b = b, a + b
    return b

'''
회고 / TIL
- 1부터 5까지 적어보니 그냥 피보나치임.
- 항상 피보나치는 반복이 더 빠르다는 것을 알고 있지만, 재귀로 푸는 것을 참을 수 없음.
'''