# https://school.programmers.co.kr/learn/courses/30/lessons/12928?language=python3

# 나의 풀이
def solution(n):
    answer = 0

    for i in range(1, n + 1):   # 1부터 n까지
        if n % i == 0:          # 나눠보면서 나머지가 0인 값들만
            answer += i         # 더함. 

    return answer


# 다른 사람의 풀이
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

'''
회고 / TIL
- 백준에서 약수 문제 많이 풀면서 n의 절반까지만 검사해도 된다는 사실을 알고 있었는데, 적용하지 않았음. 
- 기본 문제에서도 시간복잡도를 최적화하려고 노력해야겠음...
'''