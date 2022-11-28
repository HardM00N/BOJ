# https://www.acmicpc.net/problem/1003

# 나의 풀이 (Python3 76ms)
dp = [[0] * 2] * 41                                                     # dp 선언
dp[0] = [1, 0]
dp[1] = [0, 1]

def fibo(n):                                                            # 메모이제이션 활용
    if n < 2:
        return dp[n]
    else:
        if dp[n] != [0, 0]:
            return dp[n]
        else:
            dp[n] = [x + y for x, y in zip(fibo(n - 1), fibo(n - 2))]
            return dp[n]

for _ in range(int(input())):
    print(*fibo(int(input())))                                          # 결과 리스트 한 번에 출력

# 0 ->        [1, 0]
# 1 ->        [0, 1]
# 2 -> 1 + 0  [1, 1]
# 3 -> 2 + 1  [1, 2]
# 4 -> 3 + 2  [2, 3]
# 5 -> 4 + 3  [3, 5]
# 6 -> 5 + 4  [5, 8]

'''
회고 / TIL
- 기존 피보나치 DP로 풀려다가... 너무 애먹었음. 
- 그래서 0의 개수와 1의 개수에 대해서 새롭게 규칙을 찾아 DP를 만들었음. 
- 계산해야할 값이 [x, y] 쌍이 된 것 외에는 기존 피보나치 DP와 동일하게 구현하면 됨. 
'''