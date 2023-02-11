# https://www.acmicpc.net/problem/3036

# 나의 풀이 (Python3 40ms)
def GCD(a, b):                                                      # 유클리드 호제법으로 GCD 구하기
    while b:                                                        # 나머지가 0이 될 때까지
        a, b = b, a % b
    return a

N = int(input())
rings = list(map(int, input().split()))

for i in range(1, N):
    gcd = GCD(rings[0], rings[i])
    print('{}/{}'.format(rings[0] // gcd, rings[i] // gcd))

'''
- 유클리드 호제법으로 GCD 구하기
- 다른 사람의 풀이도 비슷함.
'''