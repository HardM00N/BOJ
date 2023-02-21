# https://www.acmicpc.net/problem/7795

# 나의 풀이 (Python3 360ms)
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())

    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))

    res = 0
    temp = 0                                    # 시작 변수 (시간 절약용)

    for num in A:
        start = temp
        end = len(B) - 1

        while start <= end:
            mid = (start + end) // 2

            if num <= B[mid]:
                end = mid - 1
            else:
                start = mid + 1
        
        res += end + 1
        temp = end + 1                          # 시작점 변수 초기화
    
    print(res)

'''
A = [1, 1, 3, 7, 8] -> 7은 아래의 1, 3보다 크므로, 7뒤의 8은 아래의 7부터 탐색 시작
B = [1, 3, 6]
'''

'''
회고 / TIL
- 단순 이분탐색으로 풀었을 때 548ms가 나왔는데, A도 오름차순 정렬해서 탐색 시작 변수를 이용해 시간을 더 줄였음 (360ms)
- 투 포인터로 푼 점점 많이 보임. 숙지해야겠음.
'''