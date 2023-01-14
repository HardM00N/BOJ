# https://www.acmicpc.net/problem/2504

# 나의 풀이 (Python3 36ms)
s = input()
stack = []

for i in s:
    if i == '(':
        stack.append(i)

    elif i == '[':
        stack.append(i)
    
    elif i == ']':
        if len(stack) >= 2 and str(stack[-1]).isdigit() and stack[-2] == '[':
            temp = stack.pop()
            stack.pop()
            stack.append(temp * 3)
        elif stack and stack[-1] == '[':
            stack.pop()
            stack.append(3)
        else:
            print(0)
            break
    
    elif i == ')':
        if len(stack) >= 2 and str(stack[-1]).isdigit() and stack[-2] == '(':
            temp = stack.pop()
            stack.pop()
            stack.append(temp * 2)
        elif stack and stack[-1] == '(':
            stack.pop()
            stack.append(2)
        else:
            print(0)
            break

    if len(stack) >= 2 and str(stack[-1]).isdigit() and str(stack[-2]).isdigit():
        stack.append(stack.pop() + stack.pop())

else:
    if len(stack) == 1 and str(stack[-1]).isdigit():
        print(*stack)
    else:
        print(0)

'''
회고 / TIL
- 차근차근 구현하면 되는 문제
- 나는 연산 결과도 스택에 넣었지만, 연산 결과를 변수에 저장할 수도 있음.
'''