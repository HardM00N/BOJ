# https://www.acmicpc.net/problem/2792

# 나의 풀이 (Python3 3260ms)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bosuk = [int(input()) for _ in range(M)]

start = 1
end = sum(bosuk)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    temp = []

    for i in bosuk:
        cnt += i // mid                             # 보석을 mid로 나눈 몫만큼 카운트 (7 // 6 = 1)
        
        if i % mid:                                 # 나머지가 남았으면 (7 % 6 = 1)
            cnt += 1                                # 카운트
            
    if cnt > N:                                     # 카운트가 학생 수보다 많으면 학생 당 보석량을 늘려야 함
        start = mid + 1                             # 오른쪽으로
    else:                                           # 카운트가 학생 수보다 적으면 학생 당 보석량을 줄여야 함 (같아질 때까지)
        end = mid - 1

print(end + 1)

'''
회고 / TIL
- 기타 레슨과 동일하게 풀이하면 됨.
- 보석을 받지 못하는 학생이 있더라도, 질투심 수치가 최소이면 됨.
'''