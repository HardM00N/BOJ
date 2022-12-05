# https://www.acmicpc.net/problem/11727

'''
2 x 1 -> 1
2 x 2 -> 3
2 x 3 -> 5
2 x 4 -> 11
2 x 5 -> 21
2 x 6 -> 43
2 x 7 -> 85
2 x 8 -> 171
'''

# 나의 풀이 (Python3 76ms)
import sys
sys.setrecursionlimit(10**6)

dp = [0] * 1001                                         # DP 테이블 초기화
dp[1] = 1
dp[2] = 3

def tile(n):
    if n <= 2:
        return dp[n]
    else:
        if dp[n] != 0:                                  # 메모이제이션
            return dp[n]
        else:
            dp[n] = tile(n - 1) + tile (n - 2) * 2      # 점화식 구현
            return dp[n]

print(tile(int(input())) % 10007)

'''
회고 / TIL
- 앞의 2xn 타일링의 응용 버전, 마찬가지로 규칙만 잘 찾으면 쉽게 풀 수 있음. 
- 이번에도 메모이제이션으로 필요한 연산만 할 수 있도록 구현해 봄.
'''