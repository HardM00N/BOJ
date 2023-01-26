# https://www.acmicpc.net/problem/9625

'''
A -> B
B -> BA

0 A                     (1, 0)
1 B                     (0, 1)
2 BA                    (1, 1)
3 BAB                   (1, 2)
4 BABBA                 (2, 3)
5 BABBABAB              (3, 5)
6 BABBABABBABBA         (5, 8)
'''

# 나의 풀이 (Python3 36ms)
K = int(input())
dp = [0] * 46
dp[0] = (1, 0)

def BABBA(k):
    if k == 0:
        return dp[k]
    
    else:
        tmp = BABBA(k - 1)                      # 재귀 호출
        dp[k] = (tmp[1], sum(tmp))              # (전의 두 번째 값, 전의 값들의 합)
        return dp[k]

print(*BABBA(K))

# 다른 사람의 풀이
a, b = 1, 0

for i in range(int(input())):                   # Bottom-Up
    a, b = b, b + a

print(a,b)

'''
회고 / TIL
- 쉽게 규칙을 찾을 수 있었음.
- 여기선 TC가 하나뿐이기에, 다른 사람의 풀이처럼 굳이 dp에 기록하지 않아도 되지만, TC가 여러 개라면 기록하는 편이 좋음.
'''