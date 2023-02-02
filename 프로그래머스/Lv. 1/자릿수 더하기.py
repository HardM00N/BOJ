# https://school.programmers.co.kr/learn/courses/30/lessons/12931

# 나의 풀이
def solution(n):
    total = 0
    for i in str(n):
        total += int(i)

    return total

# 다른 사람의 풀이
def sum_digit(number):
    return sum(map(int,str(number)))    # map을 활용한 풀이

'''
회고 / TIL
- str형으로 바꿔, 각 자리의 수를 쉽게 더할 수 있음. 
- 전에 비슷한 문제 int형으로 10으로 나눠가면서 어렵게 풀고 str형으로 쉽게 푼 풀이보고 좌절한 기억이 있어서 바로 str형으로 품...
'''