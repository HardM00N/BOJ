# https://www.acmicpc.net/problem/1676

# 첫 번째 풀이 (메모리 초과) -> 재귀로 풀었더니...
import sys
sys.setrecursionlimit(10**9)

N = int(input())

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

res = str(fact(N))
cnt = 0

for num in reversed(res):
    if num == '0':
        cnt += 1
    else:
        break

print(cnt)

# 두 번째 풀이
