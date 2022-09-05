'''
전쟁은 어느덧 전면전이 시작되었다.
결국 전투는 난전이 되었고, 우리 병사와 적국 병사가 섞여 싸우게 되었다. 

그러나 당신의 병사들은 흰색 옷을 입고, 적국의 병사들은 파란색 옷을 입었기 때문에 피아식별은 가능하다. 
문제는 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다. 

N명이 뭉쳤을 때 N^의 위력을 낼 수 있다. 
과연 지금 난전의 상황에서는 누가 승리할 것인가?

단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다. 
'''
import copy

N, M = map(int, input().split())
map_w = []

for _ in range(M):
    line = list(input())
    map_w.append(line)
map_b = copy.deepcopy(map_w)
    
# DFS 메서드 정의
def dfs(x, y, team, map):
    if team == 'W': 
        enemy = 'B'
    else:
        enemy = 'W'
    
    global cnt
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return False
    
    # 현재 노드를 아직 방문하지 않았다면
    if map[x][y] == team:
        # 현재 노드를 방문 처리
        map[x][y] = enemy
        cnt += 1
        
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y, team, map)
        dfs(x, y - 1, team, map)
        dfs(x + 1, y, team, map)
        dfs(x, y + 1, team, map)

        return True
    return False

cnt, result_w, result_b = 0, 0, 0
for i in range(M):
    for j in range(N):
        # 현재 위치에서 DFS 수행
        if dfs(i, j, 'W', map_w) == True:
            result_w += cnt ** 2
            cnt = 0
        elif dfs(i, j, 'B', map_b) == True:
            result_b += cnt ** 2
            cnt = 0

print(result_w, result_b)

'''
회고 / TIL
- 저번에 풀었던 음료수 얼려 먹기를 참고해서 풀었음. 
- W일 때와 B일 때를 각각 계산해야 하기 때문에 map을 2개 만들었음. 
- 원리는 알겠다만 구현이 참 쉽지 않음. 
'''