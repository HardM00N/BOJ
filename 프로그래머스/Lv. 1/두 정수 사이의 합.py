# https://school.programmers.co.kr/learn/courses/30/lessons/12912

# 나의 풀이
def solution(a, b):
    
    if a > b:                                       # a가 b보다 크다면
        a, b = b, a                                 # 자리 바꿈
    
    return sum([x for x in range(a, b + 1)])

# 다른 사람의 풀이
def adder(a, b):
    return (abs(a - b) + 1) * (a + b) // 2          # 수학 공식 n * (n + 1) / 2를 활용

'''
회고 / TIL
- 이번엔 나도 리스트 컴프리헨션으로 잘 풀었다고 생각했지만...
- 두 수 사이의 합을 계산하는 수학적 공식으로 가볍게 풀고, 절대값을 활용한 풀이를 보고 좌절함...
- 항상 더 쉽게 풀 수 있는 방법을 고민해야겠음. 
'''