# https://www.acmicpc.net/problem/11724

# 나의 풀이 (Python3 628ms)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

map = []
single_node = {str(i) for i in range(1, N + 1)}         # 단일 노드 set 초기화

for _ in range(M):
    u, v = input().split()
    
    if u in single_node:                                # u가 단일 노드에 있다면
        single_node.remove(u)                           # 이젠 단일 노드가 아니므로 제거
    if v in single_node:
        single_node.remove(v)

    if not map:                                         # 첫 번째 입력이라면
        map.append({u, v})                              # 바로 삽입

    else:                                               # 첫 번째 입력이 아니라면
        u_cnt, v_cnt = 0, 0
        u_idx, v_idx = 0, 0

        for i, m in enumerate(map):
            if u in m:                                  # map의 요소 중 u가 있다면
                u_cnt += 1
                u_idx = i                               # 해당 인덱스 저장
            elif v in m:                                # map의 요소 중 v가 있다면
                v_cnt += 1
                v_idx = i                               # 해당 인덱스 저장
        
        if u_cnt and v_cnt:                             # 서로 다른 두 set에서 u, v가 존재한다면
            map.append(map[u_idx] | map[v_idx])
            map.pop(u_idx)
            map.pop(v_idx - 1)
        elif u_cnt:
            map[u_idx].add(v)
        elif v_cnt:
            map[v_idx].add(u)
        else:
            map.append({u, v})

print(len(map) + len(single_node))                      # 연결 요소의 개수 + 단일 노드의 개수

'''
회고 / TIL
- 그래프 문제지만 DFS / BFS로 풀기도 귀찮고 무방향 그래프인지라 set로 풀릴 거 같아서 이렇게 구현함.
- TC는 통과하고 제출에서 몇 번 실패했는데, 연결이 아예 없는 단일 노드의 개수도 카운트해야했음. (근데 그럼 연결 요소라고 할 수 있나?)
- in 메서드 쓰면서 중복 제거할 때는 set가 최고...
'''