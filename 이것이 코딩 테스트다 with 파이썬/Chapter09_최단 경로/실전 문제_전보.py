'''
어떤 나라에는 N개의 도시가 있다. 
그리고 각 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시로 전보를 보내 
다른 도시로 해당 메시지를 전송할 수 있다. 

하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, 
도시 X에서 도시 Y로 향하는 통로가 설치되어 있어야 한다. 

예를 들어 X에서 Y로 향하는 통로는 있지만, Y에서 X로 통하는 통로가 없다면
Y는 X로 메시지를 보낼 수 없다. 

또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다. 

어느 날 C라는 도시에서 위급 상황이 발생했다. 그래서 최대한 많은 도시로 메시지를 보내고자 한다. 
메시지는 도시 C에서 출발해 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다. 

각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 
총 몇 개이며, 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.
'''

import sys
input = sys.stdin.readline

import heapq
INF = int(1e9)

N, M, C = map(int, input().split())
graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)

# 모든 도시 정보 입력받기
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(C):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정해, 큐에 삽입
    heapq.heappush(q, (0, C))
    distance[C] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)

cnt, max_dist = 0, 0

for i in range(1, N + 1):
    # 도달할 수 없는 경우
    if distance[i] == INF:
        continue
    else:
        cnt += 1
        max_dist = max(max_dist, distance[i])

print(cnt, max_dist)