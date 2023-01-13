# https://www.acmicpc.net/problem/5585

# 나의 풀이 (Python3 36ms)
N = int(input())
N = 1000 - N

changes = [500, 100, 50, 10, 5, 1]

cnt = 0

for change in changes:
    cnt += N // change
    N %= change

print(cnt)

'''
회고 / TIL
- 그리디의 대표적인 유형인 거스름돈 문제
- 화폐 단위가 서로의 배수이기 때문에 그리디로 해결 가능
'''