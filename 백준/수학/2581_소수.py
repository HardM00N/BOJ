# https://www.acmicpc.net/problem/2581

# 나의 풀이 (Python3 84ms)
M = int(input())
N = int(input())
primes = []                                     # 소수를 담을 리스트

for i in range(M, N + 1):
    if i == 1:                                  # 1은 소수가 아님
        continue
    
    divisor_cnt = 0                             # 약수 카운트
    
    for j in range(1, int(i ** 0.5) + 1):       # 제곱근까지만 순회
        if i % j:
            continue
        divisor_cnt += 1                        # 나눠 떨어지면 약수 카운트 + 1

    if divisor_cnt == 1:                        # 1 외에 약수가 없으면 소수이므로
        primes.append(i)                        # 소수 리스트에 추가

if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)

'''
회고 / TIL
- 제곱근까지만 순회해 약수의 개수를 구해 소수를 판별하는 방법을 사용함. 
- 다른 풀이에 비하면 아직 시간복잡도 개선의 여지가 있음.
'''