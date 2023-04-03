# https://school.programmers.co.kr/learn/courses/30/lessons/12913

# 첫 번째 풀이 (DFS : 시간 초과)
import sys
sys.setrecursionlimit(int(1e9))

scores = []

def dfs(land, row, col, score):
    score += land[row][col]                                                         # 현재 위치의 점수 누적

    if row == len(land) - 1:
        scores.append(score)                                                        # 끝에 도달하면 최종 점수 scores에 append
        return
    
    else:
        for i in range(4):
            if i == col:                                                            # 이전 행의 열과 동일한 열은 제외
                continue
            dfs(land, row + 1, i, score)                                            # DFS


def solution(land):
    for i in range(4):
        dfs(land, 0, i, 0)

    return max(scores)

# 두 번째 풀이
def solution(land):
    for i in range(1, len(land)):
        land[i][0] += max(land[i - 1][1], land[i - 1][2], land[i - 1][3])           # 직전 행까지의 최대치만 고려
        land[i][1] += max(land[i - 1][0], land[i - 1][2], land[i - 1][3])
        land[i][2] += max(land[i - 1][0], land[i - 1][1], land[i - 1][3])
        land[i][3] += max(land[i - 1][0], land[i - 1][1], land[i - 1][2])
    
    return max(land[-1])


'''
회고 / TIL
- DFS를 이용해 완전탐색을 하니 답은 나오지만 시간 초과가 발생했음.
- 점화식을 이용한 DP로만 풀어야하는 문제였음. DP 오랜만에 봐서 못 알아챘음. 다음 주 알고리즘 스터디 문제는 DP로... 
'''