# https://school.programmers.co.kr/learn/courses/30/lessons/64061

# 나의 풀이
def solution(board, moves):
    
    l = len(board)                                                              # 한 변의 길이
    visited = [[0] * l for _ in range(l)]                                       # 방문 여부 기록

    cnt = 0
    stack = []

    for m in moves:                                                             # 크레인 이동은 열 단위로
        col = m - 1

        for row in range(l):                                                    # 열이 고정되었으면, 첫 번째 인형을 만날 때까지 행을 내려감
            if not visited[row][col]:
                visited[row][col] = 1                                           # 방문한 적 없는 칸이면, 방문 처리

                if board[row][col]:                                             # 해당 위치에 인형이 있다면
                    if stack and stack[-1] == board[row][col]:                  # 스택의 마지막과 동일한 인형이라면 터뜨림
                        stack.pop()                                             # 터진 인형 제거
                        cnt += 2
                    else:                                                       # 스택의 마지막과 다른 인형이라면
                        stack.append(board[row][col])                           # 스택에 추가
                    break                                                       # 인형 하나를 집었으니, 다음 크레인 이동을 위해 중지
    return cnt

# 다른 사람의 풀이
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0                                               # visited 없이도, 인형이 있던 곳을 0으로 처리해 방문 처리 가능

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer

'''
회고 / TIL
- 거창한 문제에 비해 쉬운 문제였음.
- visited를 만드는 습관이 있는데, 굳이 그러지 않아도 되었음.
'''