# https://school.programmers.co.kr/learn/courses/30/lessons/12941

# 나의 풀이
def solution(A,B):
    result = 0

    for i, j in zip(sorted(A), sorted(B, reverse=True)):        # 오름차순 / 내림차순으로 내적
        result += i * j

    return result

'''
회고 / TIL
- 내적의 합이 최소가 되기 위해서는 각각 오름차순 / 내림차순으로 정렬 후 내적하면 됨.
- 다른 사람의 풀이도 비슷함.
'''