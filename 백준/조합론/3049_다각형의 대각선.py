# https://www.acmicpc.net/problem/3049

# 나의 풀이 (Python3 40ms)
N = int(input())

if N < 4:
    print(0)

else:
    R = min(4, N - 4)                           # 적게 계산하기 위함 (nCr = nCn-r)
    numerator = denominator = 1                 # 분자 / 분모 초기화

    for i in range(R):                          # R만큼 반복하면서
        numerator *= (N - i)                    # 분자에 곱해 나가기 ex) 100 * 99 * 98 * ...
        denominator *= (R - i)                  # 분모에 곱해 나가기 ex) 2 * 1

    print(numerator // denominator)             # 조합 결과 출력

# 다른 사람의 풀이 (Python3 40ms)
n = int(input())
print(n * (n - 1) * (n - 2) * (n - 3) // 24)

'''
- 선분 2개가 교차하기 위해서는 다각형의 꼭짓점 중에서 4점을 선택해야 한다는 것이 핵심
- 다른 사람의 풀이가 보기엔 훨씬 간단하지만, 5C4 같은 상황에서는 내 코드가 계산을 적게 함.
'''