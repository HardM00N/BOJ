# https://www.acmicpc.net/problem/2531

# 나의 풀이 (Python3 3220ms)
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
res = []

for i in range(N):
    if i + k > N:                                                           # 인덱스 넘어갈 경우
        res.append(len(set(sushi[i:N] + sushi[:(i + k) % N] + [c])))
    else:
        res.append(len(set(sushi[i:i + k] + [c])))

print(max(res))

'''
회고 / TIL
- 투 포인터 안 써도 풀리지만 겁나게 느림.
- 다른 사람의 풀이는 슬라이딩 윈도우를 활용한 것 같은데, 상당히 빠른 걸 보니 숙지해야겠음.
'''