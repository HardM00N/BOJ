# https://www.acmicpc.net/problem/1026

# 나의 풀이 (Python3 36ms)
_ = input()

A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = 0

for i, j in zip(sorted(A), sorted(B, reverse=True)):    # 하나는 오름차순, 다른 하나는 내림차순으로 곱함
    S += i * j

print(S)

'''
회고 / TIL
- 각 숫자의 곱이 최소가 되기 위해서는 작은 수는 큰 수와 곱해서 상쇄해줘야 함.
- 다른 사람의 풀이들도 대체로 비슷함.
'''