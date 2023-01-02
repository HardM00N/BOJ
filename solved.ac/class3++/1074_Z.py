# https://www.acmicpc.net/problem/1074

# 나의 풀이 (Python3 36ms)
N, r, c = map(int, input().split())
n = 2 ** N                                                              # 한 변의 길이

def find_quadrant(n, r, c, start):
    if n == 1:                                                          # 1 x 1에 도달한 경우
        print(start)                                                    # 해당 숫자 출력

    else:
        n //= 2

        if r < n and c < n:                                             # 좌측 상단
            find_quadrant(n, r, c, start)
        
        elif r < n and c >= n:                                          # 우측 상단
            find_quadrant(n, r, c - n, start + n ** 2)
        
        elif r >= n and c < n:                                          # 좌측 하단
            find_quadrant(n, r - n, c, start + n ** 2 * 2)
        
        else:                                                           # 우측 하단
            find_quadrant(n, r - n, c - n, start + n ** 2 * 3)

find_quadrant(n, r, c, 0)

'''
회고 / TIL
- 실제 맵이 필요 없기 때문에, CLASS 3++에서 앞서 풀었던 분할 정복보다 더 빠르고 쉽게 풀 수 있음.
- 분할 정복이 연습되는 느낌이라 좋았던 문제였음.
- 다른 사람의 풀이도 거의 비슷해 보임.
'''