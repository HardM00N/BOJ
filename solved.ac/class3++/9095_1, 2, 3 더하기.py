# https://www.acmicpc.net/problem/9095

'''
1 -> 1
2 -> 2
3 -> 4
4 -> 7
5 -> 13
'''

# 나의 풀이 (Python3 72ms)
dp = [0] * 11                                       # DP 테이블 초기화
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]       # 점화식

for _ in range(int(input())):
    print(dp[int(input())])

# 다른 사람의 풀이 (Python3 96ms)
N = int(input())
arr = [1, 2, 4]

for i in range(4, 11):
    arr.append(sum(arr[-3:]))                       # 슬라이싱을 이용한 좋은 풀이

for _ in range(N):
    T = int(input())
    print(arr[T - 1])

'''
회고 / TIL
- 전에 한 번 풀었던 문제고, 점화식이 쉽게 찾아져서 바로 구현했음. 
- 다른 사람의 슬라이싱을 활용한 풀이를 보니 언젠가 저렇게 써먹어야겠다는 생각이 듦. 
- 물론 연산 시간은 내 풀이가 더 빠름 ㅎㅎ...
'''