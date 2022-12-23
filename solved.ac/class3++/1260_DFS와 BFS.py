# https://www.acmicpc.net/problem/1260

from collections import deque

N, M, V = map(int, input().split())

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')

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
        graph[b].append(a)                  # 양방향이므로
        graph[b].sort()                     # 정렬 (정점의 번호가 작은 순대로 탐색하기 위함)
    graph[a].sort()                         # 정렬

dfs(graph, V, visited)
print()
bfs(graph, V, visited2)

'''
회고 / TIL
- 저번에 이코테 공부할 때 풀었던 문제지만 아직도 손에 완전히 익질 않아 이코테를 다시 읽어보면서 구현함.
- DFS / BFS에 익숙해지는 것을 더는 미루지 말자...
'''