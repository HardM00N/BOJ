# https://www.acmicpc.net/problem/2630

# 나의 풀이 (Python3 64ms)
import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

cnt0, cnt1 = 0, 0

def cnt_paper(paper, N):
    global cnt0, cnt1                                                                                   # 전체 카운트 전역 변수 선언
    c0, c1 = 0, 0                                                                                       # 임시 카운트 변수 선언

    for p in paper:
        c0 += p.count(0)
        c1 += p.count(1)

    if c0 == N ** 2 or c1 == N ** 2:                                                                    # 색종이가 하나의 색으로만 이루어져있다면
        if c0 == N ** 2:                                                                                # 그게 흰색이라면
            cnt0 += 1                                                                                   # 흰색 색종이 카운트
        else:                                                                                           # 그게 파란색이라면
            cnt1 += 1                                                                                   # 파란색 색종이 카운트
        return

    else:                                                                                               # 색종이가 하나의 색으로만 이루어져있지 않다면
        N //= 2                                                                                         # 4분할
        for row in range(2):
            for col in range(2):
                cnt_paper([p[N * col:N * (col + 1)] for p in paper[N * row:N * (row + 1)]], N)          # 재귀적으로 분할 정복

cnt_paper(paper, N)
print(cnt0, cnt1, sep='\n')

'''
회고 / TIL
- 종이의 개수를 먼저 풀어서 쉽게 풀림. (9분할 vs 4분할)
- 다행히 이 문제는 시간 초과없이 무난하게 풀렸음.
'''