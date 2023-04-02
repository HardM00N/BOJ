# https://www.acmicpc.net/problem/1359

# 나의 풀이 (Python3 44ms)
from itertools import combinations

N, M, K = map(int, input().split())
all = cnt = 0

for i in combinations(range(N), M):
    for j in combinations(range(N), M):
        if len(set(i) & set(j)) >= K:
            cnt += 1
        all += 1

print(cnt / all)

'''
회고 / TIL
- '적어도 K개'에 꽂혀서 여사건으로 풀려고 한참 삽질하다가 수 범위가 브루트포스가 가능함을 깨닫고 combinations로 풀어버림.
'''