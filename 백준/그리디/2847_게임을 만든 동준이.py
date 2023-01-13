# https://www.acmicpc.net/problem/2847

# 나의 풀이 (Python3 36ms)
N = int(input())
scores = [int(input()) for _ in range(N)][::-1]         # 점수 받아서 뒤집음

temp = scores[0]                                        # temp를 첫 번째 점수로 초기화
cnt = 0

for i in range(1, N):                                   # 두 번째 점수부터 마지막 점수까지 반복
    if temp <= scores[i]:                               # 이전 점수보다 현재 점수가 크거나 같다면
        cnt += scores[i] - temp + 1                     # 현재 점수를 이전 점수 - 1만큼 내림
        temp -= 1                                       # temp 갱신
    else:
        temp = scores[i]                                # 이전 점수보다 현재 점수가 작다면, temp 갱신
        
print(cnt)

'''
회고 / TIL
- 리스트를 뒤집어서 한조 문제처럼 풀었음.
'''