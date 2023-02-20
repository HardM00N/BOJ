# https://www.acmicpc.net/problem/1064

# 나의 풀이 (Python3 40ms)
import math

def slope(x1, y1, x2, y2):                                              # 두 점을 잇는 직선의 기울기를 계산하는 함수
        if x1 == x2:
            return 1e9
        return (y1 - y2) / (x1 - x2)

def distance(x1, y1, x2, y2):                                           # 두 점의 거리를 계산하는 함수
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

x1, y1, x2, y2, x3, y3 = map(int, input().split())

if slope(x1, y1, x2, y2) == slope(x2, y2, x3, y3):                      # 세 점이 한 직선에 있으면 평행사변형을 만들 수 없음
    print(-1.0)

else:
    perimeters = [
        (distance(x1, y1, x2, y2) + distance(x2, y2, x3, y3)) * 2,
        (distance(x1, y1, x3, y3) + distance(x2, y2, x3, y3)) * 2,
        (distance(x1, y1, x2, y2) + distance(x1, y1, x3, y3)) * 2 
    ]
    print(max(perimeters) - min(perimeters))                            # 최대 둘레 길이 - 최소 둘레 길이

'''
회고 / TIL
- 다른 풀이도 대체로 비슷함.
- 대체로 피타고라스를 사용했는데, 난 그냥 단순 거리로 둘레를 계산함.
'''