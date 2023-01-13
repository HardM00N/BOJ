# https://www.acmicpc.net/problem/2753

# 나의 풀이 (Python3 36ms)
year = int(input())

if (not year % 4 and year % 100) or not year % 400:
    print(1)
else:
    print(0)

'''
회고 / TIL
- 그냥 쉬운 문제임.
'''