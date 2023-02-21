# https://www.acmicpc.net/problem/1072

# 나의 풀이 (Python3 44ms)
X, Y = map(int, input().split())
Z = 100 * Y // X                                    # 승률 계산

if Z >= 99:
    print(-1)

else:
    start = 1
    end = 1000000000

    while start <= end:
        mid = (start + end) // 2
        
        if 100 * (Y + mid) // (X + mid) > Z:
            end = mid - 1
        else:
            start = mid + 1
        
    print(end + 1)

'''
회고 / TIL
- 전형적인 이분탐색인데... 이분탐색이 문제가 아니라 소수점 처리가 문제였음. 
- https://www.acmicpc.net/board/view/53623
'''