# https://school.programmers.co.kr/learn/courses/30/lessons/12921

# 나의 풀이
def solution(n):                                    
    prime_cnt = 0
    
    for i in range(2, n + 1):
        
        for j in range(2, int(i ** 0.5) + 1):       # 제곱근까지 탐색
            if i % j == 0:                          # 약수가 존재하면 소수가 아니므로 종료
                break
        else:
            prime_cnt += 1                          # 약수가 없다면 소수이므로 카운트                          

    return prime_cnt

# 다른 사람의 풀이 (에라토스테네스의 체, https://wikidocs.net/21638)
def solution(n):
    num = set(range(2, n + 1))                      # set 생성

    for i in range(2, n + 1):                       # 제곱근까지만 해도 됨, 이 코드는 비효율적
        if i in num:
            num -= set(range(2 * i, n + 1, i))      # 해당 i의 배수들 제외
    
    return len(num)

'''
회고 / TIL
- 처음에 n은 범위에 포함되지 않는 것으로 문제를 이해해서 잘못 풀었음.
- 소수 제곱근은 이제 국룰이고, 에라토스테네스의 체를 구현하는 여러 가지 방법들 중 하나를 익히는 것이 좋을 것 같음.
'''