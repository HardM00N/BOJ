# https://www.acmicpc.net/problem/2003

# 첫 번째 풀이 (완전 탐색 -> 시간 초과)
N, M = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0

for i in range(N):
    for j in range(i + 1, N + 1):
        if sum(nums[i:j]) == M:
            cnt += 1
            print(i, j)
            break
        if sum(nums[i:j]) > M:
            break

print(cnt)

# 두 번째 풀이 (투 포인터 / Python3 44ms)
N, M = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
interval_sum = 0
end = 0

for start in range(N):
    while interval_sum < M and end < N:         # 가능할 때까지 end를 뒤로 이동
        interval_sum += nums[end]
        end += 1

    if interval_sum == M:                       # 부분합이 M이면 카운트
        cnt += 1
    
    interval_sum -= nums[start]                 # start 뒤로 이동

print(cnt)

'''
회고 / TIL
- 실버4라 가볍게 브루트포스 시도했다가 가볍게 시간 초과
- 수열의 부분합 -> 투 포인터
'''