# https://school.programmers.co.kr/learn/courses/30/lessons/147355

# 나의 풀이
def solution(t, p):
    l = len(p)
    p = int(p)

    cnt = 0
    
    for i in range(len(t) - (l - 1)):       # 한 글자씩 이동하며 부분 문자열 탐색
        if int(t[i:i + l]) <= p:
            cnt += 1

    return cnt

# 다른 사람의 풀이
def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1

    return answer

'''
회고 / TIL
- 문자열을 하나씩 순회하며 부분 문자열을 찾아 비교하면 됨.
- 다른 사람의 풀이도 대체로 비슷함.
'''