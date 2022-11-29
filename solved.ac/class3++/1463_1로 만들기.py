# https://www.acmicpc.net/problem/1463

# 나의 풀이 (Python3 628ms)
dp = [0] * 1000001                                      # DP 테이블 선언
N = int(input())

for i in range(2, N + 1):
    # 현재의 수에서 1을 빼는 경우
    dp[i] = dp[i - 1] + 1                               # 1을 더해주는 이유는 연산 횟수를 세기 위함

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)              # 2로 나누는 경우와 1을 빼는 경우 중에서 min
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)              # 3으로 나누는 경우와 1을 빼는 경우 중에서 min

print(dp[N])

# 다른 사람의 풀이 (Python3 72ms)
s = {1:0, 2:1}                                          # 딕셔너리로 메모이제이션
def f(n):
    if n in s: return s[n]                              # 이미 테이블에 있으면 바로 반환
    m = 1 + min(f(n // 2)+ n % 2, f(n // 3) + n % 3)    # 없으면 각 연산에 대한 최솟값으로 계산    
    s[n] = m
    return m

print(f(int(input())))

'''
회고 / TIL
- 이코테 책에서 봤던 문제라서 구현엔 어려움이 없었음. 
- 다만 Bottom-Up 방식으로 구현하니 N까지 DP 테이블을 모두 채워나가느라 628ms가 걸렸음. 
- 다른 사람의 풀이를 보니 Top-Down으로 N에 필요한 연산만을 수행하고, 딕셔너리를 이용해서 시간을 대폭 줄임. 
- 여러 방법으로 풀 수 있도록 고민해보자.
'''