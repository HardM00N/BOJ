# https://school.programmers.co.kr/learn/courses/30/lessons/68935

# 나의 풀이
def solution(n):
    ternary = ''
    decimal = 0
    
    while n != 0:                               # 10진수 -> 3진수
        ternary += str(n % 3)
        n //= 3
    
    for i, bit in enumerate(ternary[::-1]):     # 뒤집은 3진수 -> 10진수
        decimal += int(bit) * 3 ** i

    return decimal

# 다른 사람의 풀이
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)                        # tmp 문자열을 3진수로 바꿈
    return answer

'''
회고 / TIL
- 문제 그대로 3진수로 변환하고 뒤집고 10진수로 변환해 풀었음.
- 다른 사람의 풀이를 보니 int()에 저런 기능이 있다니 싶다...
'''