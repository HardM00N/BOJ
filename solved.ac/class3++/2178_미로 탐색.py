# https://www.acmicpc.net/problem/2178

# 나의 풀이 (Python3 72ms)
from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        
        for a, b in zip(dx, dy):
            nx = x + a
            ny = y + b
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[N - 1][M - 1]

print(bfs(0, 0))

# 다른 사람의 풀이 (Python 48ms)
import sys

def bfs(n, m):
    # visited 배열 만들기
    # 큐 만들기
    # 인큐 하기
    global visited
    visited = [[0] * (m) for _ in range(n)]
    queue = []
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        i, j = queue.pop(0)


        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] != 0 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return visited

N, M = map(int, sys.stdin.readline().rstrip().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
bfs(N, M)
print(visited[N - 1][M - 1])

'''
회고 / TIL
- 최단 경로 미로 탐색은 BFS가 효율적이라고 함.
- BFS 코드 스스로 생각하는데 2시간 가까이 걸렸음. 바로 나올 수 있도록 숙지하자.
'''