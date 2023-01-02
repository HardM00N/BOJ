# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

meets = []
N = int(input())
for _ in range(N):
    meets.append(list(map(int, input().split())))

meets = sorted(meets, key=lambda x: (x[0], x[1]))

def find_next(m, cnt):
    for meet in meets:
        if m[1] == meet[0]:
            temp = meet
            continue
        if m[1] < meet[0]:
            

        



'''
[0, 6] [6, 10] [12, 14] -> 3
[1, 4] [5, 7] [8, 11] [12, 14] -> 4     # [5, 9] 대신 [5, 7]을 선택해야 최대임.
[2, 13] -> 1
[3, 5] [5, 7] [8, 11] [12, 14] -> 4
'''