# https://www.acmicpc.net/problem/2960

# 나의 풀이 (Python3 40ms)
def solution(N, K):
    cnt = 0
    nums = [1] * (N + 1)                        # 계수 정렬처럼 선언

    for i in range(2, N + 1):                   # 2의 배수부터 탐색
        if nums[i]:                             # 2가 존재하면
            
            for j in range(i, N + 1, i):        # 2의 배수들 0으로 처리
                if nums[j]:
                    nums[j] = 0
                    cnt += 1

                    if cnt == K:                # K번째 수일 때 종료
                        return j

print(solution(*map(int, input().split())))

'''
회고 / TIL
- 다른 사람의 풀이도 대체로 비슷함.
'''