# https://school.programmers.co.kr/learn/courses/30/lessons/12940

# 나의 풀이
def solution(n, m):
    answer = []
    
    if n > m:                               # 작은 수만큼 반복하기 위해 대소관계 확인
        n, m = m, n
    
    for i in range(n, 0, -1):               # 작은 수에서부터 1까지 내려가면서
        if n % i == 0 and m % i == 0:       # 최대공약수 찾기
            answer.append(i)
            answer.append(n * m // i)       # 두 자연수의 곱 = 최대공약수 * 최소공배수
            break
    
    return answer

# n, m = map(int, input().split())
# print(solution(n, m))

# 다른 사람의 풀이 (유클리드 호제법)
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    
    while t > 0:                            # MOD 연산의 결과가 0이 될 때까지 반복
        t = c % d
        c, d = d, t
    answer = [c, int(a * b / c)]            # MOD 연산의 결과가 0이 되었을 때 최대공약수

    return answer

'''
회고 / TIL
- GCD, LCM 문제를 접할 때마다 유클리드 호제법은 새롭게 느껴짐.
- 유클리드 호제법 관련해서는 노션 자료 공유란에 올려둠.
'''