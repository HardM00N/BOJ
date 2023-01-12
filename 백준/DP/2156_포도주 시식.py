# https://www.acmicpc.net/problem/2156

# 나의 풀이 (Python3 48ms)
# import sys
# input = sys.stdin.readline

# N = int(input())
# wines = [int(input()) for _ in range(N)]

# if N <= 2:
#     print(sum(wines))

# else:
#     dp = [0] * (N + 4)
#     dp[0] = wines[0]
#     dp[1] = dp[0] + wines[1]

#     for i in range(2, N):
#         dp[i] = max(
#             wines[i] + dp[i - 2],
#             wines[i] + wines[i - 1] + dp[i - 3],
#             wines[i] + wines[i - 1] + dp[i - 4]
#         )

#     print(max(dp))