# https://school.programmers.co.kr/learn/courses/30/lessons/135808

# 나의 풀이
def solution(k, m, score):
    boxes = len(score) // m                             # 박스의 개수 구하기
    score = sorted(score, reverse=True)                 # 점수 내림차순으로 정렬

    res = 0

    for i in range(boxes):                              # 박스의 개수만큼 반복하면서
        res += score[m * (i + 1) - 1] * m               # 각 박스에서 가장 낮은 점수 * 사과 개수

    return res

# 다른 사람의 풀이
def solution(k, m, score):
    return sum(sorted(score)[len(score) % m::m]) * m    # 오름차순으로 정렬해서 m씩 상승

'''
회고 / TIL
- 정렬하고, 높은 점수의 사과부터 담으면 쉬움.
'''