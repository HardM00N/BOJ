'''
동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혀 있다. 
미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 

동빈이의 위치는 (1, 1)이고, 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 

이 때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 
미로는 반드시 탈출할 수 있는 형태로 제시된다. 

이 때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.
'''
from collections import deque

N, M = map(int(input))

_map = []
for _ in range(N):
    _map.append(list(map(int, input())))

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 소스코드 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if _map[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if _map[nx][ny] == 1:
                _map[nx][ny] = _map[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return _map[N - 1][M - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))