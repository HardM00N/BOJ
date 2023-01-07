# https://www.acmicpc.net/problem/2667

# 나의 풀이 (Python3 36ms)
import sys
input = sys.stdin.readline

graph = []
N = int(input())

for _ in range(N):
    graph.append(list(map(int, input().strip())))           # 그래프 입력 받기

def dfs(x, y):
    global inside_cnt
    
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False

    if graph[x][y] == 1:                                    # 방문한 적 없으면
        inside_cnt += 1                                     # 아파트 수 카운트 (단지 내의 아파트 수)
        graph[x][y] = 0                                     # 방문 처리
    
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        
        return inside_cnt                                   # 단지 내의 아파트 수 리턴

    return False

cnt = 0
apts = []

for i in range(N):                                          # 전체 그래프를 돌며
    for j in range(N):
        inside_cnt = 0                                      # 단지 내 아파트 수 초기화
        apt = dfs(i, j)
        
        if apt:                                             # 아파트 단지가 있었으면
            cnt += 1                                        # 단지의 수 카운트
            apts.append(apt)                                # 해당 단지 내의 아파트 수 추가

print(cnt)
for apt in sorted(apts):
    print(apt)

'''
회고 / TIL
- 이코테의 음료수 얼려 먹기의 응용판인 것 같음. (단지별 아파트 개수 카운트)
- DFS에 좀 더 익숙해지자.
'''