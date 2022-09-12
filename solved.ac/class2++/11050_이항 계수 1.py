'''
자연수 N과 정수 K가 주어졌을 때 이항 계수를 구하는 프로그램을 작성하시오. 
'''

N, K = map(int, input().split())

def binomial(N, K):
    if ( K == 0 or N == K):
        return 1
    return binomial(N  - 1, K - 1) + binomial(N - 1, K)

print(binomial(N, K))

'''
회고 / TIL
- 파스칼의 삼각형, 조합 등 이항 계수의 성질을 안다면 재귀적으로 풀 수 있음. 
- 사실 재귀적으로 풀면 중복으로 계산되는 부분이 생김 -> DP로 기록해나가면서 풀면 해결되지만... 오늘은 쉽게 풀고 싶었다...
'''