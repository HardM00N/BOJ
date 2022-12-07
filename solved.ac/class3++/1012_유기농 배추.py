# https://www.acmicpc.net/problem/1012

# 나의 풀이 (Python3 52ms)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):                                              # DFS로 특정 노드 방문 후, 연결된 모든 노드 방문
    if x <= -1 or x >= M or y <= -1 or y >= N:              # 주어진 그래프를 벗어나는 경우 종료
        return False
    
    if graph[x][y] == 1:                                    # 현재 노드를 아직 방문하지 않았다면
        graph[x][y] = 0                                     # 현재 노드 방문 처리

        dfs(x - 1, y)                                       # 상하좌우 재귀적으로 호출
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True
    return False    

for _ in range(int(input())):                               # 테스트 케이스
    
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(M)]       # 그래프 초기화
    
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1                                     # 배추가 있는 위치를 1로

    cnt = 0                                                 # 배추흰지렁이 카운트
    for i in range(M):
        for j in range(N):
            if dfs(i, j) == True:
                cnt += 1
    
    print(cnt)

'''
회고 / TIL
- 이코테에서 DFS 공부할 때 음료수 얼려 먹기와 거의 같은 문제였음.
- DFS와 아직은 조금 낯가리는 사이지만, 점점 친해져야겠다. 
- 백준 풀이 2등 달성!
'''