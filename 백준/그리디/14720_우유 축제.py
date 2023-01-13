# https://www.acmicpc.net/problem/14720

# 나의 풀이 (Python3 36ms)
N = int(input())
stores = list(map(int, input().split()))

cnt, milk = 0, 0                                            # 딸기 우유부터 시작

for store in stores:

    if milk == store:                                       # 찾는 우유와 가게가 일치하면
        cnt += 1                                            # 카운트
        milk += 1                                           # 우유도 카운트

    if milk == 3:                                           # 모든 우유를 다 마셨으면 리셋
        milk = 0

print(cnt)

'''
회고 / TIL
- 단순한 문제였음.
'''