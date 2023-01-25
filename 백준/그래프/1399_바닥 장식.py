# https://www.acmicpc.net/problem/1388

# 나의 풀이 (Python3 56ms)
N, M = map(int, input().split())
board = [input() for _ in range(N)]
visited = [[0] * M for _ in range(N)]

def dfs(x, y, shape):

    if x <= -1 or x >= N or y <= -1 or y >= M or board[x][y] != shape:      # 인덱스가 board 범위를 벗어나거나 해당 위치의 모양이 기존의 shape과 다르다면
        return False

    if not visited[x][y]:                                                   # 방문한 적 없다면
        visited[x][y] = 1                                                   # 방문 처리

        if shape == '|':                                                    # shape이 '|'라면 세로 방향 탐색
            dfs(x - 1, y, shape)
            dfs(x + 1, y, shape)
        else:                                                               # shape이 '-'라며 가로 방향 탐색
            dfs(x, y - 1, shape)
            dfs(x, y + 1, shape)

        return True
    
    return False

cnt = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j, board[i][j]) == True:
            cnt += 1

print(cnt)

# 다른 사람의 풀이
L = [input() for _ in range(int(input().split()[0]))]
print(sum(len([p for p in r.split('|') if p]) for r in L) + sum(len([q for q in ''.join(x).split('-') if q]) for x in zip(*L)))

'''
회고 / TIL
- 이코테의 음료수 얼려 먹기와 CLASS 3++의 단지번호붙이기와 유사한 문제
- 다른 사람의 풀이를 보니, 그래프를 사용하지 않고도 split으로 풀 수 있었음.
'''