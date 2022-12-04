# https://www.acmicpc.net/problem/11726

'''
1 -> 1
2 -> 2
3 -> 3
4 -> 5
'''

# 나의 풀이 (재귀, 메모이제이션, Python3 68ms)
import sys
sys.setrecursionlimit(10**6)

dp = [0] * 1001                                         # DP 테이블 초기화
dp[1] = 1
dp[2] = 2

def tile(n):                                            # 메모이제이션
    if n <= 2:
        return dp[n]
    else:
        if dp[n] != 0:                                  # 이미 있는 값이면 그대로 출력
            return dp[n]
        else:
            dp[n] = tile(n - 1) + tile(n - 2)           # 없으면 재귀적으로 호출
            return dp[n]

print(tile(int(input())) % 10007)

'''
회고 / TIL
- 예전에도 풀었던 기본적인 DP 문제임. 
- 예전에는 반복적으로 풀어서 88ms가 걸렸는데, 이번에는 메모이제이션으로 필요한 dp만 계산해서, 시간을 줄였음. 
'''