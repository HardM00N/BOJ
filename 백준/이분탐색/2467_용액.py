# https://www.acmicpc.net/problem/2467

# 나의 풀이 (Python3 732ms)
N = int(input())
sol = list(map(int, input().split()))

min = int(1e10)
mins = []

for i in range(N - 1):                              # i는 고정하고
    start = i + 1                                   # start부터 end까지 더할 대상(mid)을 탐색
    end = N - 1
    
    while start <= end:
        mid = (start + end) // 2
        _sum = sol[i] + sol[mid]
        
        if abs(_sum) < min:                         # 더한 절댓값이 최소면
            min = abs(_sum)                         # min 최신화
            mins = [sol[i], sol[mid]]               # 해당 값들 기록
        
        if _sum < 0:                                # 합이 0보다 작으면 오른쪽으로
            start = mid + 1
        else:                                       # 합이 0보다 크면 왼쪽으로
            end = mid - 1
            
print(*mins)

'''
회고 / TIL
- 창민님이 풀어보자고 해서 푼 문제
- 전날 이분탐색 문제를 두 개 풀고 풀어서 나름 수월했음.
'''