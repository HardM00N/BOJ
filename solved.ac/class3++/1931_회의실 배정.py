# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

meets = []
avail_meets = []

N = int(input())
visited = [0] * N
print(visited)

# for _ in range(N):
#     meets.append(list(map(int, input().split())))

# meets = sorted(meets, key=lambda x: (x[0], x[1]))

# for meet in meets:

'''
[0, 6] [6, 10] [12, 14] -> 3
[1, 4] [5, 7] [8, 11] [12, 14] -> 4     # [5, 9] 대신 [5, 7]을 선택해야 최대임.
[2, 13] -> 1
[3, 5] [5, 7] [8, 11] [12, 14] -> 4
'''