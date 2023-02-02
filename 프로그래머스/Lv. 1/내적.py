# https://school.programmers.co.kr/learn/courses/30/lessons/70128

# 나의 풀이
def solution(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))  # 리스트의 대응되는 인덱스끼리 곱함. 

# 다른 사람의 풀이
def solution(a, b):
    return sum([x * y for x, y in zip(a, b)])       # zip을 활용한 풀이

'''
회고 / TIL
- 나름 파이써닉하게 풀었다고 생각했지만 zip이 있었다...
'''