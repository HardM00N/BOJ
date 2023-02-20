# https://www.acmicpc.net/problem/1358

# 나의 풀이 (Python3 44ms)
import sys, math
input = sys.stdin.readline

W, H, X, Y, P = map(int, input().split())
cnt = 0

def distance(x1, y1, x2, y2):                                   # 좌표 간 거리를 계산하는 함수
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

for _ in range(P):
    x, y = map(int, input().split())

    if X <= x <= X + W and Y <= y <= Y + H:                     # 선수의 좌표가 가운데 사각형에 속할 경우
        cnt += 1

    else:                                                       # 선수의 좌표가 두 반원에 속할 경우
        if distance(x, y, X, Y + H // 2) <= H // 2:
            cnt += 1
        elif distance(x, y, X + W, Y + H // 2) <= H // 2:
            cnt += 1
    
print(cnt)

'''
회고 / TIL
- 상위 5개 풀이 모두 비슷했음. 
- 아무래도 좌표 계산으로 풀 수 있는 문제다 보니 대체로 비슷하다고 생각됨.
'''