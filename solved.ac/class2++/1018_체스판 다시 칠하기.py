'''
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M x N 크기의 보드를 찾았다. 
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 
지민이는 이 보드를 잘라서 8 x 8 크기의 체스판으로 만들려고 한다. 

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각혀은 다른 색으로 칠해져 있어야 한다. 
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지 뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다. 

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8 x 8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
당연히 8 x 8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오. 
'''

N, M = map(int, input().split())
board = []
cnts = []
for _ in range(N):
    board.append(input())

# 체스판 시작점 순회
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        count_W, count_B = 0, 0

        # 왼쪽 위가 흰색인 경우, 검은색인 경우에 대해 각각 count
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if k % 2 == 0:
                    if l % 2 == 0:
                        if board[k][l] != 'W':
                            count_W += 1
                        else: 
                            count_B += 1
                    else:
                        if board[k][l] != 'B':
                            count_W += 1
                        else: 
                            count_B += 1
                else:
                    if l % 2 == 0:
                        if board[k][l] != 'B':
                            count_W += 1
                        else: 
                            count_B += 1
                    else:
                        if board[k][l] != 'W':
                            count_W += 1
                        else: 
                            count_B += 1
        cnts.append(count_W)
        cnts.append(count_B)

print(min(cnts))

'''
회고 / TIL
- 효율적인 풀이가 마땅히 생각나지 않아서 문제 그대로 순회하면서 개수를 세도록 풀었음. 
- 다른 사람 풀이 찾아보니 거의 이렇게 푼 거 같아서 안심했음. 역시 브루트 포스...
'''