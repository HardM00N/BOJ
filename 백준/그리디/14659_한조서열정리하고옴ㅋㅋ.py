# https://www.acmicpc.net/problem/14659

# 나의 풀이 (Python3 48ms)
N = int(input())
archers = list(map(int, input().split()))

temp = archers[0]                               # 첫 번째 활잡이부터 비교
res, cnt = [], 0

for i in range(1, N):                           # 두 번째부터 마지막 활잡이까지만 반복
    if temp > archers[i]:                       # 다음 활잡이가 전의 활잡이보다 작으면
        cnt += 1                                # 카운트

    else:                                       # 다음 활잡이가 더 큰 경우
        temp = archers[i]                       # temp 갱신
        res.append(cnt)                         # 이전까지의 카운트 기록
        cnt = 0

    if i == N - 1:                              # 마지막 카운트 저장
        res.append(cnt)

print(max(res))                                 # 기록된 카운트 중 최댓값 출력

'''
회고 / TIL
- 쉬운 문제인데 2번 틀려서 다시 고민해보니 마지막 반복 때의 카운트를 append하지 않았음.
- 문제를 이해하면 수월함.
'''