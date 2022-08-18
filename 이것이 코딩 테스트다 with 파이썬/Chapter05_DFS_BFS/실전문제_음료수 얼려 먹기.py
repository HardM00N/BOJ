'''
N x M 크기의 얼음 틀이 있다. 구명이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 

이 때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
'''

# 답안 예시
N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1

        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True
    return False

# 모든 노드(위치)에 대해 음료수 채우기
result = 0
for i in range(N):
    for j in range(M):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)   # 정답 출력

'''
회고 / TIL
- DFS, BFS 알고리즘을 공부하고 풀었는데도 어려워서 결국 예시 답안을 봤다. 
- 단순히 그래프에서 깊이적인 개념으로만 이해했었는데, 여기서는 갈 수 있는 노드를 파고드는 개념이었다. 
- 처음에는 뭔가 BFS로 풀려고 시도했었는데, 실패했다. 아직 두 알고리즘을 체득하지 못한 것 같다. 
- 추가로, 뭔가 저번 구현 챕터에 나왔던 게임 개발처럼도 풀 수 있을 것 같은데, 귀찮았다... 오늘은 장렬히 패배...
'''