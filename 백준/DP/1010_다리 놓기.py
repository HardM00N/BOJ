# https://www.acmicpc.net/problem/1010

# 나의 풀이 (메모이제이션 활용, Python3 64ms / 30840KB)
import sys
input = sys.stdin.readline

dp = [0] * 31                                       # 팩토리얼 기록할 dp 선언
dp[0], dp[1] = 1, 1                                 # 0!, 1! = 1, 1

def fact(x):                                        # 팩토리얼 구현
    if x <= 1:
        return dp[x]
    else:
        if dp[x] != 0:                              # dp에 해당 값이 이미 있으면 바로 리턴
            return dp[x]
        else:
            dp[x] = x * fact(x - 1)                 # dp에 값이 없으면 재귀 호출
            return dp[x]

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(fact(M) // (fact(N) * fact(M - N)))       # 조합 공식으로 계산

# 다른 사람의 풀이 (Python3 56ms / 28776KB)
from sys import stdin

input = stdin.readline
dp=[0 for _ in range(31)]
dp[0] = 1
dp[1] = 1

for i in range(2, 31):
    dp[i] = i * dp[i-1]

for tc in range(int(input())):
    w, e = map(int, input().split())
    print((dp[e]) // (dp[e - w] * dp[w]))

'''
회고 / TIL
- 확실히 예전에 처음 DP 문제 풀 때보다 수월하게 구현했음. (많이 풀어보는 것이 정답...)
- 문제와 테스트 케이스를 보니까 조합인 것 같아서 팩토리얼을 먼저 구현하고, 조합 공식으로 계산함. 
- 다른 사람의 풀이는 크게 차이나지 않는데, 애초에 30까지만 주어지기 때문에 미리 다 계산하고 들어가는 것 같음. 
'''