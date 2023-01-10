# https://www.acmicpc.net/problem/24460

# 나의 풀이 (Python3 1292ms / PyPy3 780ms)
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def special_prize(N, graph):                                    # N, graph를 입력받아 두 번째로 작은 요소 리턴

    if N == 1:                                                  # 더 분할할 수 없다면, 해당 값 리턴
        return graph[0][0]
    
    else:                                                       # 분할 가능하다면 4분할 재귀 호출
        N //= 2

        temp = [
            special_prize(N, [g[:N] for g in graph[:N]]),
            special_prize(N, [g[N:] for g in graph[:N]]),
            special_prize(N, [g[:N] for g in graph[N:]]),
            special_prize(N, [g[N:] for g in graph[N:]])
        ]

        return sorted(temp)[1]                                  # 두 번째로 작은 요소 리턴

print(special_prize(N, graph))

'''
회고 / TIL
- 분할 정복 재밌음.
'''