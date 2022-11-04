'''
스택은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 
스택은 자료를 넣는 입구와 자료를 뽑는 입구가 같아, 
제일 나중에 들어간 자료가 제일 먼저 나오는 LIFO 특성을 가진다. 

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓아서 하나의 수열을 만들 수 있다. 
이 때, 스택에 push하는 순서는 반드시 오름차순을 지킨다고 하자. 

임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 

이를 계산하는 프로그램을 작성하라. 
'''

stack, results = [], []
check = 0

now = 1

for _ in range(int(input())):
    num = int(input())

    # 스택 push
    while now <= num:
        stack.append(now)
        results.append('+')
        now += 1
    
    # 스택 pop
    if stack[-1] == num:
        stack.pop()
        results.append('-')
    
    # 불가능할 경우
    else:
        check = 1

if check:
    print('NO')
else:
    for result in results:
        print(result)

'''
회고 / TIL
- 너무 어렵게 생각해서 복잡하게 풀다가 꼬여서 결국 답지를 참고함. 
- 로직이 생각보다 간단했음. 내 생각엔 불가능한 예외에 대해 여러 조건이 필요하다고 생각했지만 그렇지 않았음. 
- 실버2부터 슬슬 쉽지 않은 느낌이 듦...
'''