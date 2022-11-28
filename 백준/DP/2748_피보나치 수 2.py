# https://www.acmicpc.net/problem/2748

# 첫 번째 풀이 (시간 초과)
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

print(fibo(int(input())))

# 두 번째 풀이 (메모이제이션 활용, Python3 68ms)
dp = [0] * 91                                       # fibo 결과 기록할 dp 선언
dp[1] = 1

def fibo(n):
    if n < 2:                                       # n이 0 혹은 1이라면 그대로 리턴
        return dp[n] 
    else:
        if dp[n] != 0:                              # dp[n]이 이미 계산된 값이라면 그대로 출력
            return dp[n]
        else:                                       # 계산된 적 없다면 재귀적으로 계산하고, 기록
            dp[n] = fibo(n - 1) + fibo(n - 2)
            return dp[n]

print(fibo(int(input())))

'''
회고 / TIL
- 오랜만에 푸는 DP 문제지만 다행히 가장 기본인 피보나치 문제라 쉽게 구현했음. 
- 브론즈 1 문제이길래 단순 재귀로 풀었다가 시간초과나서 바로 메모이제이션으로 다시 풀었음... 브론즈도 빡셈. 
'''