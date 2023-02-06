# https://www.acmicpc.net/problem/11004

# 나의 풀이 (Python3 3908ms / PyPy3 2680ms)
N, K = map(int, input().split())
nums = sorted(map(int, input().split()))
print(nums[K - 1])

'''
회고 / TIL
- 단순 정렬로 풀면 시간이 오래 걸리는 듯함.
'''