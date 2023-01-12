# https://www.acmicpc.net/problem/2156

# 나의 풀이 (Python3 44ms)
import sys
input = sys.stdin.readline

N = int(input())
wines = [int(input()) for _ in range(N)]

if N <= 2:                                                                                      # N이 2 이하면 합이 최댓값
    print(sum(wines))

else:
    dp = [0] * N
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    dp[2] = max(wines[0] + wines[1], wines[0] + wines[2], wines[1] + wines[2])                  # 3번째 와인을 포함하지 않은 case도 포함

    for i in range(3, N):
        dp[i] = max(dp[i - 1], wines[i] + dp[i - 2], wines[i] + wines[i - 1] + dp[i - 3])       # 마찬가지로 i번째 와인을 포함하지 않은 경우도 포함

    print(dp[-1])                                                                               # 마지막 값이 마실 수 있는 최댓값
    
'''
회고 / TIL
- class 3++의 계단 오르기와 매우 흡사하지만, i번째를 꼭 마시지 않아도 된다는 차이점이 있음.
- 그 부분까지 고려해서 dp를 계산해나가야 함.
'''