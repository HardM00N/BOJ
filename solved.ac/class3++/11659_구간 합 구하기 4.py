# https://www.acmicpc.net/problem/11659

# 첫 번째 풀이 (시간 초과)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

for _ in range(M):
    i, j = map(int, input().split())    
    print(sum(nums[i - 1:j]))

# 두 번째 풀이 (Python3 324ms, PyPy3 240ms)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0] * N                                  # 각 인덱스까지의 합을 미리 저장할 리스트
sums[0] = nums[0]

for i in range(1, N):
    sums[i] = nums[i] + sums[i - 1]             # N까지의 누적합 계산

for _ in range(M):
    i, j = map(int, input().split())

    if i == j:                                  # i와 j가 같으면, 그 자신 값 출력
        print(nums[i - 1])
    else:
        if i == 1:                              # 첫 번째부터 시작이면, j까지의 합만 출력
            print(sums[j - 1])
        else:
            print(sums[j - 1] - sums[i - 2])    # j까지의 합에서 i 이전까지의 합을 뺌

'''
회고 / TIL
- 무턱대고 풀었다가 시간 초과에 부딪혀서, 미리 누적합을 다 구하고 j까지의 합 - i 이전까지의 합으로 계산하니 해결됨. 
- 다른 사람의 풀이를 보니 itertools의 accumulate이란게 있더라... 연산 시간은 큰 차이가 없음. 
'''