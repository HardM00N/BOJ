'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 

단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 

정점 번호는 1번부터 N번까지이다. 
'''
from collections import deque

N, M, V = map(int, input().split())

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    # 큐 (queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = []
for _ in range(N + 1):
    graph.append([])
visited = [False] * (N + 1)
visited2 = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)
        graph[b].sort()
    graph[a].sort()

dfs(graph, V, visited)
print()
bfs(graph, V, visited2)

'''
회고 / TIL
- DFS, BFS가 보면 이해되는데 아직 코드가 손에 붙질 않아서 기존에 썼던 DFS / BFS 코드를 참고했다. 
- 여기서는 정점 간의 연결 정보를 단편적으로 받기 때문에 graph를 만들 때 추가 작업이 필요했음. (서로 연결된 정보, 정렬)
'''