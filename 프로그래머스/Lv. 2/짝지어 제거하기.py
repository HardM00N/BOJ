# https://school.programmers.co.kr/learn/courses/30/lessons/12973

# 나의 풀이
def solution(s):
    stack = [s[0]]                          # 스택에 첫 글자 넣고 시작
    
    for i in s[1:]:                         # 두 번째 글짜부터 스택에 넣으면서
        if stack and i == stack[-1]:        # 스택이 비어있지 않다면, 스택의 top과 비교
            stack.pop()                     # 같다면, 짝지어 제거해야하므로 pop()
        else:
            stack.append(i)                 # 스택이 비었거나 스택의 top과 다르다면, append
    
    return 0 if stack else 1                # 스택이 비었으면 1, 차있으면 0

'''
회고 / TIL
- 다른 사람의 풀이도 대체로 비슷함.
'''