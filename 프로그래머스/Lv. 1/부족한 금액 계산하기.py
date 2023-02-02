# https://school.programmers.co.kr/learn/courses/30/lessons/82612

# 나의 풀이
def solution(price, money, count):
    total = 0
    
    for i in range(1, count + 1):
        total += price * i
    
    if money >= total:
        return 0
    else:
        return total - money

# 다른 사람의 풀이
def solution(price, money, count):
    return abs(min(money - sum([price * i for i in range(1, count + 1)]), 0))

'''
회고 / TIL
- 위 두 풀이는 같은 내용이지만 아래가 훨씬 우아하다...
- min으로 처리하는 부분이 인상적임.
'''