# https://www.acmicpc.net/problem/17247

# 나의 풀이 (Python3 112ms)
import sys
input = sys.stdin.readline

def taxi_geo():
    N, M = map(int, input().split())
    graph = [list(input().split()) for _ in range(N)]
    
    start = []
    
    for i in range(N):                                                          # 그래프를 돌면서
        for j in range(M):
            
            if graph[i][j] == '1':                                              # 1이 나오면
                if not start:
                    start.append(i)
                    start.append(j)
                else:
                    return abs(i - start[0]) + abs(j - start[1])                # 택시 거리 리턴

print(taxi_geo())

# 다른 사람의 풀이
from sys import stdin
n, m = map(int, stdin.readline().split())
graph = [ stdin.readline().rstrip().replace(' ', '') for _ in range(n) ]
coords = []

for idx, row in enumerate(graph) : 
    if row.find('1') != -1 : 
        coords.append([idx+1, row.find('1')+1])                                 # 문자열과 find를 이용한 풀이

print(abs(coords[0][0]-coords[1][0]) + abs(coords[0][1] - coords[1][1]))

'''
회고 / TIL
- 오랜만에 보는 택시 기하 문제
- 대체로 풀이가 비슷하나, 다른 사람의 풀이는 find()를 사용한 것이 인상적이었음.
'''