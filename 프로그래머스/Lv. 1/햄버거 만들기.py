# https://school.programmers.co.kr/learn/courses/30/lessons/133502

# 나의 풀이
def solution(ingredient):
    cnt = 0
    stack = ingredient[:3]                          # 3개 미리 넣고 시작

    for i in ingredient[3:]:
        stack.append(i)

        if stack[-4:] == [1, 2, 3, 1]:
            # stack = stack[:-4]                    # stack이 매우 길 경우 시간 초과
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            cnt += 1

    return cnt

'''
회고 / TIL
- 1등 풀이랑 거의 비슷함. (내껀 미리 3칸을 넣고 시작함)
'''