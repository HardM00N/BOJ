# https://www.acmicpc.net/problem/16173

# 나의 풀이 (Python3 36ms)
import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def dfs(x, y):

    if x < 0 or y < 0 or x >= N or y >= N:                          # map을 벗어난 경우
        return False
    
    distance = map[x][y]                                            # 다음 이동 거리

    if distance == -1:                                              # 마지막 칸에 도달했다면
        print('HaruHaru')
        exit()                                                      # 종료

    if not visited[x][y]:                                           # 방문한 적이 없으면
        visited[x][y] = 1                                           # 방문 처리
        dfs(x + distance, y)                                        # 오른쪽
        dfs(x, y + distance)                                        # 아래쪽

dfs(0, 0)
print('Hing')                                                       # 코드가 종료되지 않았다면 도달하지 못했으므로

# 다른 사람의 풀이
N = int(input())
graph=[list(map(int,input().split())) for _ in range(N)]

base = [[0] * N for _ in range(N)]

def dfs(x,y):

    if x < 0 or x >= N or y < 0 or y >= N or base[x][y] == 1:
        return False
    
    if graph[x][y] == -1:                                           # 끝
        base[x][y] = 1
        return False
    
    base[x][y] = 1                                                  # 방문 기록 남기기
    dfs(x + graph[x][y], y)
    dfs(x, y + graph[x][y])

dfs(0,0)
if base[-1][-1] == 1:                                               # 마지막 칸을 방문했다면
    print('HaruHaru')
else:
    print('Hing')

'''
회고 / TIL
- DFS로 풀었는데, 마지막 칸까지 방문했을 경우 끝내는 처리가 잘 생각이 안나 그 부분은 답지를 참고함.
- 다른 사람의 풀이를 보니 visited를 이용해서 마지막 칸 방문 여부를 판별할 수 있었음.
'''