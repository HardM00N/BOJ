# https://www.acmicpc.net/problem/1676

# 첫 번째 풀이 (메모리 초과) -> 재귀로 풀었더니...
import sys                              # recursion depth error 해결책...
sys.setrecursionlimit(10**9)

N = int(input())

def fact(n):                            # 팩토리얼 재귀함수
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

res = str(fact(N))
cnt = 0

for num in reversed(res):               # 팩토리얼 결과를 문자열로 만들어 뒤집음. 
    if num == '0':                      # 0이 나오면 카운트
        cnt += 1
    else:
        break

print(cnt)

# 두 번째 풀이 (반복문, Python3 76ms)
N = int(input())

def fact(n):
    res = 1
    if n < 2:
        return 1
    else:
        for i in range(n, 1, -1):
            res *= i
        return res


res = str(fact(N))
cnt = 0

for num in reversed(res):               # 팩토리얼 반복문 함수
    if num == '0':
        cnt += 1
    else:
        break

print(cnt)


# 다른 사람의 풀이 (천상계 풀이...)
N = int(input())
print(N // 5 + N // 25 + N // 125)      # 5의 배수의 개수에 따라 0의 개수를 판별

'''
회고 / TIL
- 무턱대로 재귀로 풀었다가 recursion detph의 벽에 부딪혔고, recursionlimit을 변경해봤지만 메모리 초과에 부딪혔음. 
- 메모이제이션으로 구현해야하나 싶었지만 일단 반복문으로 팩토리얼을 구현하니 풀렸음.
- 0이 아닌 숫자가 나올 때까지 0의 개수를 카운트하는 부분은 문자열로 변환해 뒤집어서 해결함. 
- 다른 사람의 천상계 풀이를 보니 5로 나눠진 몫만큼 0이 나타나는 것을 이용해 풀었음.... 25인 경우는 5 x 5이므로 0이 하나씩 더 들어가므로 따로 카운팅함. 
- 문제를 풀 때 규칙성을 발견해 풀도록 노력해야겠음. 
'''