# https://www.acmicpc.net/problem/11047

# 나의 풀이 (Python3 72ms)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
cnt = 0

for _ in range(N):
    coins.append(int(input()))

for coin in sorted(coins, reverse=True):                # 내림차순으로 정렬
    if coin > K:                                        # 동전이 금액보다 크면 다음 작은 동전으로
        continue
    else:                                               # 동전이 금액보다 작으면 최대한 그 동전으로 나눔
        cnt += K // coin
        K %= coin

print(cnt)

# 다른 사람의 풀이 (시간은 동일)
N, K = map(int,input().split())
a = [int(input()) for _ in "A" * N]
s = 0
for i in a[::-1]:s += K // i; K %= i
print(s)

'''
회고 / TIL
- N이 최대 10개 들어오고, 각 동전은 배수이기 때문에 그리디로 쉽게 풀 수 있음. 
- 다른 사람의 풀이도 코드를 간단하게 쓰긴 했지만, 메모리와 소요시간은 동일했음. 
- 그래도 줄여쓸 수 있도록 노력해봐야겠음. 
'''