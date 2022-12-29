# https://www.acmicpc.net/problem/2217

# 첫 번째 풀이 (Python3 시간 초과)
from itertools import combinations
import sys
input = sys.stdin.readline

ropes = []
max_weight = 0                                      # 최대 중량 초기화

N = int(input())

for _ in range(N):
    ropes.append(int(input()))

for i in range(1, N + 1):
    for j in combinations(ropes, i):                # N개씩 조합 생성
        comb_weight = min(j) * i                    # 조합의 최솟값 * 조합의 길이가 조합의 중량

        if max_weight < comb_weight:                # 조합의 중량이 최대 중량보다 크면
            max_weight = comb_weight                # 최대 중량 갱신

print(max_weight)

# 두 번째 풀이 (Python3 108ms)
import sys
input = sys.stdin.readline

ropes = []
max_weight = 0                                      # 최대 중량 초기화

N = int(input())

for _ in range(N):
    ropes.append(int(input()))

ropes = sorted(ropes)                               # 로프 오름차순 정렬

for i in range(N):
    comb_weight = ropes[i] * (N - i)                # 정렬된 로프가 순서대로 최솟값이므로, 로프의 개수와 곱해 조합의 중량 계산

    if max_weight < comb_weight:
        max_weight = comb_weight

print(max_weight)

'''
회고 / TIL
- 처음에 조합을 떠올려 combinations로 풀었더니 시간 초과가 발생함.
- 어차피 조합에서 최소 로프 길이에 따라 조합의 중량이 결정되기 때문에 모든 조합을 조사하는 것은 비효율적이었음.
- 따라서 로프를 오름차순으로 정렬한 후, 하나씩 순회해 조합의 중량을 계산함. 
'''