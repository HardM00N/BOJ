# https://school.programmers.co.kr/learn/courses/30/lessons/12934

# 나의 풀이
def solution(n):
    sqrt = n ** (1/2)
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    else:
        return -1

'''
회고 / TIL
- 차근차근 구현함. 
- 다른 사람 풀이도 거의 비슷해서 리뷰는 생략함. 
'''