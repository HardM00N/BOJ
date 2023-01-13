# https://www.acmicpc.net/problem/11000

# 나의 풀이 (Python3 396ms)
import heapq
import sys
input = sys.stdin.readline

N = int(input())
classes = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])       # 시작 시간 기준으로 오름차순 정렬

queue = []

heapq.heappush(queue, classes[0][1])                                                            # 첫 번째 강의 종료 시간 heapq에 넣기

for i in range(1, N):
    if classes[i][0] < queue[0]:                                                                # 현재 강의의 시작 시간이 heapq의 종료 시간보다 빠르다면
        heapq.heappush(queue, classes[i][1])                                                    # heapq에 추가
    else:                                                                                       # 현재 강의의 시작 시간이 heapq의 종료 시간보다 늦다면
        heapq.heapreplace(queue, classes[i][1])                                                 # 해당 강의 heapq에서 제거 후 현재 강의 추가

print(len(queue))                                                                               # heapq의 길이가 강의실의 최소 개수

'''
회고 / TIL
- CLASS 3++의 회의실 배정과 달리 단순히 정렬만으로 해결하지 못했음.
- 문제의 알고리즘 분류를 확인하니 우선순위 큐가 있어서, heapq를 찾아보고 적용해서 겨우 풀었음.
- 처음엔 강의 정보가 정렬되어서 들어온다고 생각했으나, 그렇지 않아서 정렬을 해줘야 했음.
- heapq랑 더 친해져야할 것 같음...
'''