# https://www.acmicpc.net/problem/3986

# 나의 풀이 (Python3 140ms)
import sys
input = sys.stdin.readline

cnt = 0

for _ in range(int(input())):
    word = input().strip()
    stack = []

    for w in word:                  # 단어의 한 글자씩 가져와서
        if not stack:               # 스택이 비었으면 그대로 append
            stack.append(w)
            continue

        if stack:                   # 스택이 비어있지 않다면 top과 비교
            if stack[-1] == w:      # top과 같다면 top을 pop
                stack.pop()
            else:                   # top과 다르다면 그대로 append
                stack.append(w)

    if not stack:                   # 반복이 끝나고 스택이 비었다면 좋은 단어이므로
        cnt += 1                    # 카운트

print(cnt)

'''
회고 / TIL
- 전형적인 스택 문제, 괄호 문제와 같음.
'''