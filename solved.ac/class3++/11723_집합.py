# https://www.acmicpc.net/problem/11723

# 첫 번째 풀이 (Python3 3552ms / 메모리 30840KB)
import sys
input = sys.stdin.readline

S = [0] * 21                        # 공집합 선언

for _ in range(int(input())):
    cmd = input().split()

    if cmd[0] == 'add':    
        S[int(cmd[1])] = 1          # 숫자가 추가되면 해당 인덱스를 1로
        
    elif cmd[0] == 'remove':        # 숫자가 제거되면 해당 인덱스를 0으로
        S[int(cmd[1])] = 0
        
    elif cmd[0] == 'check':         # check는 현재 인덱스 상태 그대로 출력
        print(S[int(cmd[1])])
        
    elif cmd[0] == 'toggle':        # 상태 반전 출력
        if S[int(cmd[1])]:
            S[int(cmd[1])] = 0
        else:
            S[int(cmd[1])] = 1

    elif cmd[0] == 'all':
        S = [1] * 21
        
    elif cmd[0] == 'empty':
        S = [0] * 21

# 두 번째 풀이 (Python3 3096ms / 메모리 30840KB)
import sys
input = sys.stdin.readline

S = []                      

for _ in range(int(input())):
    cmd = input().split()

    if cmd[0] == 'add':    
        if cmd[1] not in S:
            S.append(cmd[1])          
        
    elif cmd[0] == 'remove':        
        if cmd[1] in S:
            S.remove(cmd[1])
        
    elif cmd[0] == 'check':        
        if cmd[1] in S:
            print(1)
        else:
            print(0)
        
    elif cmd[0] == 'toggle':       
        if cmd[1] in S:
            S.remove(cmd[1])
        else:
            S.append(cmd[1])

    elif cmd[0] == 'all':
        # S = [str(i) for i in range(1, 21)]
        S = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    elif cmd[0] == 'empty':
        S = []

'''
회고 / TIL
- 메모리 제한이 4MB라 메모리 공간을 최소한으로 사용하기 위해 계수 정렬처럼 리스트를 활용함. (첫 번째 풀이)
- 다른 사람의 풀이보다 메모리는 적게 사용하지만, 시간이 오래 걸림. (두 풀이 모두)
- 다른 방법을 더 고민해봐야겠음. 
'''