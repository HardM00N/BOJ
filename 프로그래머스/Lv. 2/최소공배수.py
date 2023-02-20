# https://school.programmers.co.kr/learn/courses/30/lessons/12953

# 나의 풀이
def GCD(a, b):                                  # GCD (유클리드 호제법)
    while b:
        a, b = b, a % b
    return a

def solution(arr):
    a = arr[0]
    
    for i in range(1, len(arr)):
        a = a * arr[i] // GCD(a, arr[i])        # LCM

    return a

'''
회고 / TIL
- 다른 사람의 풀이를 보니 fractions의 gcd 함수가 있었음.
- 근데 이런 거 외우는 것보다 호제법 구현이 쉽기 때문에 앞으로도 만들어서 쓸 듯.
'''