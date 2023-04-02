# https://school.programmers.co.kr/learn/courses/30/lessons/161990

# 나의 풀이
def solution(wallpaper):
    lux = luy = 51
    rdx = rdy = -1

    for x, line in enumerate(wallpaper):
        for y, icon in enumerate(line):
            if icon == '#':                 # 바탕화면에 아이콘이 있다면
                lux = min(lux, x)           # x 좌표의 최솟값 갱신
                luy = min(luy, y)           # y 좌표의 최솟값 갱신
                rdx = max(rdx, x + 1)       # x 좌표 + 1의 최댓값 갱신
                rdy = max(rdy, y + 1)       # y 좌표 + 1의 최댓값 갱신

    return [lux, luy, rdx, rdy]

'''
회고 / TIL
- 문제는 길지만 로직은 심플함. 
- 아이콘이 위치한 최소 좌표와 최대 좌표를 찾아서 그대로 반환하면 됨.
'''