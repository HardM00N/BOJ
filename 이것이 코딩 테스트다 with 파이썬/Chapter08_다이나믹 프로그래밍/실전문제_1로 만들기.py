'''
정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다. 

- X가 5로 나누어 떨어지면, 5로 나눈다.
- X가 3으로 나누어 떨어지면, 3으로 나눈다.
- X가 2로 나누어 떨어지면, 2로 나눈다.
- X에서 1을 뺀다.

정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만들려고 한다. 

연산을 사용하는 횟수의 최솟값을 출력하시오.
'''

X = int(input())

dp = [0] * (X + 1)

# 다이나믹 프로그래밍 진행 (Bottom-Up)
for i in range(2, X + 1):
    # 현재의 수에서 1을 빼는 경우
    dp[i] = dp[i - 1] + 1

    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[i])

'''
회고 / TIL
- DP 개념과 예제 문제를 풀고 접한 문제라 자신감 넘치게 도전했으나 recursion error에 부딪혀 답지를 참고함. 
- Top-Down 방식으로 모든 경우의 수에 대해 연산 횟수를 count하고 최솟값을 출력하게 하려고 했으나 recursion error...
- 답지를 참고하니 Bottom-Up으로 접근해야 하는 것 같다. 
- DP에서는 유명한 문제라고 함. (백준에도 동일한 문제가 있음)
'''