# https://www.acmicpc.net/problem/9461

# 나의 풀이 (Python3, 80ms)
dp = [0] * 101                          # DP 테이블 최기화
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6, 101):
    dp[i] = dp[i - 1] + dp[i - 5]       # 점화식 구현

for _ in range(int(input())):
    print(dp[int(input())])

'''
회고 / TIL
- 그림에 있는 규칙대로 점화식을 구현하니 쉽게 풀렸음. 
- DP에 익숙해져가는 것인가...
- 다른 사람의 풀이도 유사해서 리뷰 스킵함. 
'''