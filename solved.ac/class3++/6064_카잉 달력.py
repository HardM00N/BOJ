# https://www.acmicpc.net/problem/6064

import sys
input = sys.stdin.readline

N = int(input())
steps = [int(input()) for _ in range(N)]


if N <= 2:
    print(sum(steps))

else:
    dp = [0] * N
    dp[0] = steps[0]
    dp[1] = dp[0] + steps[1]
    dp[2] = max(steps[2] + steps[1], steps[2] + steps[0])

    
    for i in range(3, N):
        dp[i] = max(steps[i] + steps[i - 1] + dp[i - 3], steps[i] + dp[i - 2])
    
    print(dp[N - 1])

'''
전전칸에서 정해야 할게 -> 다음칸을 밟을지 다다음칸을 밟을지
'''