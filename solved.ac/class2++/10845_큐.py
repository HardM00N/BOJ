'''
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오. 

명령은 총 여섯 가지이다. 

- push X : 정수 X를 큐에 넣는 연산이다. 
- pop : 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다. 
- size : 큐에 들어있는 정수의 개수를 출력한다. 
- empty : 큐가 비어있으면 1, 아니면 0을 출력한다. 
- front : 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다. 
- back : 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다. 
'''

import sys
input = sys.stdin.readline

queue = []

for _ in range(int(input())):
    cmd = input().split()

    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)

'''
회고 / TIL
- 앞서 풀었던 10828번 스택 문제와 동일하게 큐의 각 메서드를 차근차근 단순히 구현하면 됨. 
- 문제를 풀면서 오랜만에 자료구조가 리마인드 되어서 좋았음. 
'''