def solution(ingredient):
    cnt = 0
    stack = ingredient[:3]

    for i in ingredient[3:]:
        stack.append(i)

        if stack[-4:] == [1, 2, 3, 1]:
            # stack = stack[:-4]
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            cnt += 1

    return cnt

# while 1:
#     try:
#         print(solution(input().split()))
#     except:
#         break