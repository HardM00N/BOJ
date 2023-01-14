# https://www.acmicpc.net/problem/2512

# 나의 풀이 (Python3 60ms)
N = int(input())
needs = list(map(int, input().split()))
cap = int(input())

if sum(needs) <= cap:                                   # 예산이 초과되지 않았다면 바로 출력
    print(max(needs))

else:                                                   # 예산 초과라면 적절한 mid 값 이분탐색
    start = 1
    end = max(needs)

    while start <= end:
        mid = (start + end) // 2
        total = 0
        
        for need in needs:
            if need <= mid:
                total += need
            else:
                total += mid

        print(start, end, mid, total)

        if total <= cap:                                # total이 예산보다 작으면
            start = mid + 1                             # mid를 좀 더 올려도 됨
        else:
            end = mid - 1

    print(start - 1)

'''
회고 / TIL
- 이분 탐색의 start, end 업데이트 조건을 잘 확인하자.
- 구현 자체는 쉬웠던 문제
'''