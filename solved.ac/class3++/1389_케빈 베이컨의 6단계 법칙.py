# https://www.acmicpc.net/problem/1389

# 나의 풀이 (Python3 88ms)
import sys
input = sys.stdin.readline

INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]                             # 그래프 무한으로 초기화

for a in range(1, N + 1):                                                   # 자기 자신으로의 비용은 0으로 초기화
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N + 1):                                                   # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

sums = []
for a in range(1, N + 1):
    sums.append(sum(graph[a]))                                              # 케빈 베이컨 수 계산

print(sums.index(min(sums)) + 1)                                            # 가장 케빈 베이컨 수가 작은 사람 출력

# 다른 사람의 풀이 (BFS)
import sys

[n, m] = list(map(int, sys.stdin.readline().split()))
graph = [[] for i in range(n + 1)]
kebin = [0] * (n + 1)

for i in range(m):
    [a, b] = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n + 1):
    graph[i].sort()

for start in range(n + 1):
    bfs_s = {start}
    depth_list = []
    node = [start]

    while True:
        depth_list.append(node)
        new_node = []
        for i in node:
            for j in graph[i]:
                if j not in bfs_s:
                    bfs_s.add(j)
                    new_node.append(j)
        if len(new_node) == 0:
            break
        node = new_node

    for i, d in enumerate(depth_list):
        # print(f'{i}: {d}', len(d))
        kebin[start] += len(d) * i
    # print(depth_list)

k = 5000
result = 0
for i in range(1, n + 1):
    if kebin[i] < k:
        k = kebin[i]
        result = i
print(result)

'''
회고 / TIL
- 모든 정점 사이의 최단 경로를 구하는 문제라 플로이드 워셜을 떠올렸으나, 구현이 잘 기억나지 않아 이코테 책을 참고함.
- 어찌됐든 한 정점과 연결된 다른 정점들 사이의 최단 경로들의 합이 가장 작은 케이스를 찾는 문제였음.
- BFS로도 풀 수 있을 것 같긴 했는데, 다른 사람의 풀이를 보니 복잡하다. 그래프는 아직 어렵다...
'''