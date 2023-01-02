# https://www.acmicpc.net/problem/1697

# 나의 풀이 (Python3 124ms)
from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001                                      # 직선 내에서 최댓값까지의 방문 기록

queue = deque()
queue.append(N)                                             # 큐에 수빈이 초기 위치 삽입

while queue:
    x = queue.popleft()

    if x == K:                                              # 동생 위치와 같아지면
        print(visited[x])                                   # 해당 위치까지 걸린 시간 (트리의 깊이) 출력
        break                                               # 반복문 종료

    for i in (x - 1, x + 1, x * 2):                         # 세 가지 이동 방식 중에서
        if 0 <= i <= 100000 and not visited[i]:             # 범위 내에서 가능한 연산이고 방문한 적 없는 곳이라면
            visited[i] = visited[x] + 1                     # 해당 위치까지 걸린 시간을 기록해 방문 처리
            queue.append(i)

# 다른 사람의 풀이
import sys

def f(n, k):
    if n >= k: return n - k
    if k == 1: return 1
    if k % 2: return min(f(n, k + 1), f(n, k - 1)) + 1     
    
    return min(k - n, f(n, k // 2) + 1)

print(f(*map(int, sys.stdin.readline().split())))

'''
회고 / TIL
- 기껏 이코테 펼쳐놓고... 이것저것 참고하면서 그래프로 풀었더만 다른 사람 풀이를 보니 아주 간단하게 풀어놨음.
- 문제 유형에 국한되어서 생각하지 말자.
'''