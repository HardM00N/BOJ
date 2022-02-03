def solution(n):
    
    dp = [0] * n
    dp[0], dp[1] = 1, 2
    
    if n == 1 or n == 2:
        print(dp[n-1])
        
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n-1] % 1000000007