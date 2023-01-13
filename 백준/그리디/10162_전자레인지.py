# https://www.acmicpc.net/problem/10162

# 나의 풀이 (Python3 40ms)
T = int(input())

A, B, C = 300, 60, 10

if T % C:
    print(-1)

else:
    for i in (A, B, C):
        print(T // i, end=' ')                          # 가장 큰 버튼부터 차례대로 나눠주기
        T %= i

'''
회고 / TIL
- 가장 큰 수로 먼저 나눠주는 것이 최소한 버튼을 누르는 방법임.
- 다른 사람들의 풀이도 비슷해 생략함.
'''