# https://www.acmicpc.net/problem/1931

# 나의 풀이 (Python3 264ms)
import sys
input = sys.stdin.readline

meets = []
cnt, end = 0, 0                                                 # 카운트, 종료 시간 초기화

N = int(input())
for _ in range(N):
    meets.append(list(map(int, input().split())))

for meet in sorted(meets, key=lambda x: (x[1], x[0])):          # 1. 종료 시간 2. 시작 시간으로 정렬
    if end <= meet[0]:                                          # 종료 시간보다 시작 시간이 크거나 같다면 회의 가능
        cnt += 1
        end = meet[1]                                           # 종료 시간 갱신

print(cnt)                                                      # 회의 카운트 출력

'''
회고 / TIL
- 종료 시간으로 먼저 정렬하고, 그 중에서 시작 시간으로 정렬하는 것이 포인트였음.
- 생각보다 쉽게 풀렸는데, 다른 사람의 풀이는 유난히 천차만별이라 생략함.
'''