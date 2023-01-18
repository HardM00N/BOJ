# https://www.acmicpc.net/problem/9372

# 나의 풀이 (Python3 220ms)
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = 1                                          # 방문 처리
    
    cnt = 0
    
    while queue:
        x = queue.popleft()

        for next in graph[x]:                               # 연결된 국가들 탐색
            if visited[next]:
                continue
            else:
                queue.append(next)                          # 방문한 적 없으면 큐에 추가
                visited[next] = 1
                cnt += 1                                    # 간선 개수 카운트
    
    return cnt

for _ in range(int(input())):
    N, M = map(int, input().split())
    
    graph = [[] for _ in range(N)]
    visited = [0 for _ in range(N)]

    for _ in range(M):
        A, B = map(int, input().split())
        graph[A - 1].append(B - 1)                          # 양방향 그래프
        graph[B - 1].append(A - 1)

    res = 0

    for i in range(N):
        if not visited[i]:
            res += bfs(i)
    
    print(res)

# 다른 사람의 풀이
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    print(n - 1)                                            # 모든 국가가 연결되어 있으니 최소 간선은 n - 1개
    
    for _ in range(m):
        input()

'''
회고 / TIL
- 오랜만에 그래프 풀이라 카운트하는 부분에서 시간을 좀 소모했음.
- 실컷 풀고 나니 아주 쉽게 풀 수 있는 방법이 있어서 현타가 옴.
- 더 찾아보니 최소 신장 트리 / DFS로도 풀 수 있었음.
'''