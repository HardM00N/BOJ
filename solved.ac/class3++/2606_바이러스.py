# https://www.acmicpc.net/problem/2606

# 나의 풀이 (Python3 92ms) -> BFS
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

visited = [False] * (N + 1)                 # 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph, start, visited):             # BFS 정의   
    queue = deque([start])                  # 큐 (Queue) 구현을 위해 deque 라이브러리 사용
    visited[start] = True                   # 현재 노드를 방문 처리
    
    while queue:                            # 큐가 빌 때까지 반복 
        v = queue.popleft()                 # 큐에서 하나의 원소를 뽑아 출력
        global cnt                          # 바이러스에 걸리는 컴퓨터의 수 카운트
        cnt += 1
        
        for i in graph[v]:                  # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True

cnt = 0
bfs(graph, 1, visited)
print(cnt - 1)                              # 1번 컴퓨터 자기 자신 제외하고 출력

# 다른 사람의 풀이 (Python3 72ms) -> DFS
import sys

def dfs(n):
    Heap.append(n)
    for v in V[n]:
        if v not in Heap:
            dfs(v)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

V = [[] for _ in range(N + 1)]
Heap = []

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    V[a].append(b)
    V[b].append(a)

dfs(1)
print(len(Heap) - 1)

'''
회고 / TIL
- 내가 제일 약한 DFS / BFS 문제였음... BFS 구현은 이코테의 코드를 참고함.
- 다른 사람의 풀이를 보니 굳이 deque에서 pop하지 않고, cnt 대신 deque의 길이를 반환해도 됨.
- 실버에서 최대한 DFS / BFS에 익숙해지자! 
'''