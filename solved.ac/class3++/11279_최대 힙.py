# https://www.acmicpc.net/problem/11279

# 나의 풀이 (Python3 124ms)
import heapq
import sys
input = sys.stdin.readline

queue = []

for _ in range(int(input())):
    x = int(input())

    if x >= 1:
        heapq.heappush(queue, -x)               # 파이썬에서는 최대 힙을 지원하지 않으므로 - 부호를 붙여 삽입
    elif x == 0:
        if queue:
            print(-heapq.heappop(queue))        # 출력할 때 다시 - 부호를 붙이면 최대 힙 구현
        else:
            print(0)

'''
회고 / TIL
- 최소 힙 문제와 거의 동일한데, 음수로 처리해 최대 힙을 구현하는 부분이 포인트였음.
'''