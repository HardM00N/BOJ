# https://www.acmicpc.net/problem/2579

# 나의 풀이 (Python3 76ms)
N = int(input())
steps = []                                                                              # 계단 점수를 저장할 리스트

for _ in range(N):
    steps.append(int(input()))

if N <= 2:                                                                              # 계단이 2개라면, 합을 출력
    print(sum(steps))

else:
    dp = [0] * N                                                                        # dp 테이블 초기화
    dp[0] = steps[0]
    dp[1] = dp[0] + steps[1]
    dp[2] = max(steps[2] + steps[1], steps[2] + steps[0])                               # 3번째 계단까지는 단순 계산

    for i in range(3, N):                                                               # 그 이상부터는 발생하는 규칙 활용
        dp[i] = max(steps[i] + steps[i - 1] + dp[i - 3], steps[i] + dp[i - 2])          # 전 칸으로부터 1칸 건너뛸 것인지, 2칸 건너뛸 것인지

    print(dp[N - 1])

# 다른 사람의 풀이
from sys import stdin

a, b, c = 0, 0, 0                                                                       # 비교에 필요한 세 칸만 선언
n = int(stdin.readline())

for _ in range(n):
    pb = int(stdin.readline())
    d_0, d_1, d_2 = max(b, c), a + pb, b + pb                                           # 세 칸끼리의 가중합 업데이트
    a, b, c = d_0, d_1, d_2

print(max(d_2, d_1))                                                                    # 마지막은 두 칸 전까지의 합과 한 칸 전까지의 합 중에서 비교

'''
회고 / TIL
- 이런 스타일의 DP도 꽤나 전형적인 것 같은데 아직은 빠른 시간 내에 규칙 찾기가 쉽지 않음.
- 다른 사람의 풀이에서 비교에 필요한 변수 3개만 선언한 점이 인상적이었음... 
'''