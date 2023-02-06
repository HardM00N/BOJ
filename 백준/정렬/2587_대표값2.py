# https://www.acmicpc.net/problem/2587

# 나의 풀이 (Python3 52ms)
import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(5)]
print(sum(nums) // 5, sorted(nums)[2], sep='\n')

'''
회고 / TIL
- 단순 정렬 문제
'''