'''
현민이는 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 중이다. 
캐릭터가 있는 장소는 1 x 1 크기의 정사각형으로 이뤄진 N x M 크기의 직사각형으로,
각각의 칸은 육지 또는 바다이다. 캐릭터는 동서남북 중 한 곳을 바라본다. 

맵의 각 칸은 (A, B)로 나타낼 수 있고,
A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다. 

캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다. 
캐릭터의 움직임을 설정하기 위해 정해놓은 매뉴얼은 이러하다. 

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향 (반시계 방향으로 90도 회전한 방향)부터 
차례대로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음
왼쪽으로 한 칸을 전진한다. 
왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 
바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 
단, 이 때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다. 

현민이는 위 과정을 반복적으로 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트하려고 한다. 
매뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.
'''

# 내 풀이

n, m = map(int, input().split())
x, y, d = map(int, input().split())

_map = []
for i in range(n):
    _map.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

_map[x][y] = '1'
count = 1
dir_count = 0

while True:
    d -= 1  # 왼쪽 바라보기
    if d < 0:
        d = 3
    
    nx = x + dx[d]
    ny = y + dy[d]

    if _map[nx][ny] == 0:
        _map[nx][ny] = '1'
        x, y = nx, ny
        count += 1
        dir_count = 0
        continue
    else:
        dir_count += 1
    
    if dir_count == 4:  # 방향 유지한채 후진
        nx = x - dx[d]
        ny = y - dy[d]

        if _map[nx][ny] == 0:
            x, y = nx, ny
        else:
            break   # 못 감
        dir_count = 0

print(count)

# 4-4.py 답안 예시
# N, M을 공백을 기준으로 구분해 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성해 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 x 좌표, y 좌표, 방향 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀 있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)

'''
회고 / TIL
- 차근차근 진행하면 되는 문제인데, 도저히 머리가 아파서 풀이를 참고했다. 
- 2차원 리스트 append 하는 부분은 늘 헷갈리는 것 같다. 잘 숙지하자. 
- 지도 변수로 map을 선언했다가 map()과 겹쳐 오류가 났고 (이런 실수를...), _map으로 진행함. 
- 구현 문제에서 방향을 다룰 때는 dx, dy를 만들어 다루는 것이 효과적이라고 함. 
'''