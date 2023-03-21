# https://www.acmicpc.net/problem/12605

# 나의 풀이 (Python3 40ms)
import sys
input = sys.stdin.readline

for i in range(int(input())):
    words = list(input().split())
    print('Case #{}: '.format(i + 1), end='')
    print(' '.join(words[::-1]))                # 역순 출력

'''
회고 / TIL
- 단순히 역순으로 출력하면 되는 쉬운 문제
'''