# https://school.programmers.co.kr/learn/courses/30/lessons/172928

# 나의 풀이
def find_start(park):                                                   # 시작 위치 찾기
    for x, line in enumerate(park):
        for y, target in enumerate(line):
            if target == 'S':
                return x, y
                
def solution(park, routes):
    x, y = find_start(park)
        
    for route in routes:
        nx, ny = x, y                                                   # 이동할 위치를 임시로 저장

        for _ in range(int(route[-1])):                                 # n칸만큼 반복
            if route[0] == 'N':                                         # 북
                if nx - 1 < 0 or park[nx - 1][ny] == 'X':               # 맵을 벗어나거나 장애물이면 break
                    break
                nx -= 1

            elif route[0] == 'S':                                       # 남
                if nx + 1 >= len(park) or park[nx + 1][ny] == 'X':
                    break
                nx += 1

            elif route[0] == 'W':                                       # 서
                if ny - 1 < 0 or park[nx][ny - 1] == 'X':
                    break
                ny -= 1

            else:                                                       # 동
                if ny + 1 >= len(park[0]) or park[nx][ny + 1] == 'X':
                    break
                ny += 1
        
        else:                                                           # 끝까지 break문이 걸리지 않았다면, 즉 이동 가능하다면 새 위치로 이동 (for - else)
            x, y = nx, ny

    return [x, y]

'''
회고 / TIL
- 문제에 충실한 정직한 풀이
'''