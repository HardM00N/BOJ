# https://www.acmicpc.net/problem/1940

# 나의 풀이 (Python3 52ms)
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
nums = sorted(map(int, input().split()))

cnt = 0
start, end = 0, N - 1

while start < end:
    if nums[start] + nums[end] == M:
        cnt += 1
        start += 1
        end -= 1
    
    elif nums[start] + nums[end] < M:
        start += 1
    else:
        end -= 1

print(cnt)

'''
회고 / TIL
- 수들의 합 2와는 달리, 정렬 후 양 끝에서 좁혀가는 전형적인 투 포인터
- 다른 사람들의 풀이도 비슷함.
'''