# https://school.programmers.co.kr/learn/courses/30/lessons/42842

'''
1. xy = yellow
2. (x + 2)(y + 2) = yellow + brown

2번 전개 후 1번 대입 -> 2x + 2y + 4 = brown
'''

# 나의 풀이
def solution(brown, yellow):
    for y in range(1, int(yellow ** 0.5) + 1):              # 약수 탐색
        
        if yellow % y == 0:
            x = yellow // y                                 # 약수 찾았으면

            if 2 * (x + y + 2) == brown:                    # 조건 확인
                return [x + 2, y + 2]                       # 정렬 필요 없음


# 다른 사람의 풀이
def solution(brown, yellow):
    w = (brown / 2)
    h = 2
    while w >= h:
        if (w - 2) * (h - 2) == yellow:
            return [w, h]
        w -= 1
        h += 1

'''
XXXXX
XXXXX

XXXX
XOOX
XXXX

이렇게 하나씩 탐색하면서 노란 타일읙 개수를 체크, 마찬가지로 정렬 필요 없음.
'''

'''
회고 / TIL
- 약수로 푼 풀이도 있고, 규칙으로 푼 풀이, 근의 공식으로 푼 풀이 등 다양함.
'''