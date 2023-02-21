# https://school.programmers.co.kr/learn/courses/30/lessons/76502

# 나의 풀이
def solution(s):

    if len(s) % 2:                                          # 길이가 홀수면 가차없이 0
        return 0

    for _ in range(len(s)):

        stack = []
        cnt = 0                                             # 괄호 덩어리 개수 세기

        for i in s:                                         # 스택에 괄호 넣기
            if stack and i in ')}]':
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                    if not stack:                           # pop을 했는데 괄호가 비었다 -> 한 덩어리
                        cnt += 1

                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                    if not stack:                           # pop을 했는데 괄호가 비었다 -> 한 덩어리
                        cnt += 1

                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                    if not stack:                           # pop을 했는데 괄호가 비었다 -> 한 덩어리
                        cnt += 1
                
                else:                                       # 짝이 맞지 않는 닫힌 괄호 들어오면 실패!
                    cnt = 0
                    break

            elif i in '({[':
                stack.append(i)
            else:                                           # 스택 비었는데 닫힌 괄호 들어오면 실패!
                cnt = 0
                break
               
        if not stack and cnt:                               # 스택도 비었고 괄호 덩어리 개수도 셌으니
            return cnt                                      # 종료
        
        s = s[1:] + s[0]                                    # 괄호 회전
    
    return cnt

'''
정확성  테스트
테스트 1 〉	통과 (0.98ms, 10.3MB)
테스트 2 〉	통과 (0.25ms, 10.1MB)
테스트 3 〉	통과 (0.39ms, 10.4MB)
테스트 4 〉	통과 (0.38ms, 10.2MB)
테스트 5 〉	통과 (0.14ms, 10.1MB)
테스트 6 〉	통과 (0.27ms, 10.4MB)
테스트 7 〉	통과 (0.14ms, 10.2MB)
테스트 8 〉	통과 (0.14ms, 10.1MB)
테스트 9 〉	통과 (0.14ms, 10.2MB)
테스트 10 〉	통과 (0.14ms, 10.2MB)
테스트 11 〉	통과 (0.22ms, 10.1MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.4MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
'''

# 다른 사람의 풀이
def is_valid(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif stack[-1] == '(':
            if ch==')': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '{':
            if ch=='}': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '[':
            if ch==']': stack.pop()
            else: stack.append(ch)

    return False if stack else True

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += is_valid(s[i:]+s[:i])
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (177.72ms, 10.2MB)
테스트 2 〉	통과 (162.54ms, 10.2MB)
테스트 3 〉	통과 (260.85ms, 10.3MB)
테스트 4 〉	통과 (191.24ms, 10.2MB)
테스트 5 〉	통과 (131.00ms, 10.1MB)
테스트 6 〉	통과 (128.65ms, 10.1MB)
테스트 7 〉	통과 (136.91ms, 10.3MB)
테스트 8 〉	통과 (139.12ms, 10.2MB)
테스트 9 〉	통과 (133.54ms, 10.1MB)
테스트 10 〉	통과 (123.79ms, 10.2MB)
테스트 11 〉	통과 (129.20ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
'''

'''
회고 / TIL
- 다른 사람들은 모두 정말로 문자열을 회전시켜서 스택에 넣어서 올바른 케이스의 개수를 세는 것 같았음. 
- 나는 회전 중에 한 가지 올바른 케이스를 발견할 때, 괄호의 덩어리 개수를 바로 리턴함. 
- [](){}은 괄호의 덩어리가 3개 -> 그럼 어차피 이 3개가 순서만 바뀌어서 나오므로 답은 3임. 더 반복할 필요 X
- 따라서 시간이 월등히 빠름.
'''