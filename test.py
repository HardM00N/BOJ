def solution(N, K):
    cnt = 0

    nums = [1] * (N + 1)
    nums[0], nums[1] = 0, 0    

    for i in range(2, N + 1):
        if nums[i]:
            for j in range(i, N + 1, i):
                if nums[j]:
                    nums[j] = 0
                    cnt += 1

                if cnt == K:
                    return j

while 1:
    try:
        N, K = map(int, input().split())
        print(solution(N, K))
    except:
        break