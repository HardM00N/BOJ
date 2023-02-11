# https://www.acmicpc.net/problem/9613

# 나의 풀이 (Python4 44ms)
from itertools import combinations
import sys
input = sys.stdin.readline

def GCD(a, b):                                  # 유클리드 호제법
    while b:
        a, b = b, a % b
    return a

for _ in range(int(input())):
    nums = list(map(int, input().split()))
    total = 0

    for i in combinations(nums[1:], 2):         # 2개씩 조합
        total += GCD(*i)

    print(total)

'''
회고 / TIL
- 유클리드 호제법 + combination
- 다른 사람의 풀이도 비슷함.
'''