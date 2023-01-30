from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = 1
    
    cnt = 0
    
    while queue:
        x = queue.popleft()

        for next in graph[x]:
            if visited[next]:
                continue
            else:
                queue.append(next)
                visited[next] = 1
                cnt += 1
    
    return cnt

for _ in range(int(input())):
    N, M = map(int, input().split())
    
    graph = [[] for _ in range(N)]
    visited = [0 for _ in range(N)]

    for _ in range(M):
        A, B = map(int, input().split())
        graph[A - 1].append(B - 1)
        graph[B - 1].append(A - 1)

    res = 0

    for i in range(N):
        if not visited[i]:
            res += bfs(i)
    
    print(res)