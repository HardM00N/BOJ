'''
 여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 '순서대로', 즉 먼저 요청된 것을 먼저 인쇄한다. 
 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO에 따라 인쇄가 된다. 
 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발했는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다. 

 1. 현재 Queue의 가장 앞에 있는 문서의 '중요도'를 확인한다. 
 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치한다. 그렇지 않다면 바로 인쇄를 한다. 

 예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3이라면 C를 인쇄하고, 다음으로 D를 인쇄하고, A, B를 인쇄하게 된다. 

 여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 
 예를 들어 C 문서는 1번째로, A문서는 3번째로 인쇄되게 된다. 
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    _, M = map(int, input().split())
    priority = list(map(int, input().split()))
    cnt = 0
    
    while 1:
        if M == 0:                                      # 우리가 추적할 숫자(인덱스 M)가 맨 앞일 때
            if priority[0] == max(priority):            # 이 값이 중요도가 가장 높다면
                priority.pop(0)
                cnt += 1
                print(cnt)                              # 큐에서 삭제하면서 출력
                break
            else:                                       # 이 값보다 더 중요도가 높은 값이 존재한다면
                priority.append(priority.pop(0))        # 이 값을 맨 뒤로 보냄
                M = len(priority) - 1                   # 인덱스(M)는 한 칸 앞으로 이동
        else:                                           # 우리가 추적할 숫자(인덱스 M)가 맨 앞이 아닐 때
            if priority[0] == max(priority):
                priority.pop(0)
                cnt += 1
            else:
                priority.append(priority.pop(0))
            M -= 1                                      # 동일한 작업을 수행하면서 인덱스(M)는 한 칸 앞으로 이동

'''
회고 / TIL
- 문제가 얼핏 복잡해 보이지만 차근차근 구현함. 
- priority[M]의 위치 추적을 위해 index인 M을 잘 관리해야 했음. 
- 실질적으로 프린트될 때(pop이 일어날 때) 마다 cnt를 올려, 우리가 추적하는 priority[M]이 출력될 때 최종 cnt를 출력함. 
'''