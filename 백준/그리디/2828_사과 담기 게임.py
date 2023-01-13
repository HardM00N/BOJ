# https://www.acmicpc.net/problem/2828

# 나의 풀이 (Python3 36ms)
import sys
input = sys.stdin.readline

_, M = map(int, input().split())
apples = [int(input()) for _ in range(int(input()))]

left, right = 1, M                                          # 바구니의 왼쪽, 오른쪽 위치 초기화
cnt = 0

for apple in apples:
    if apple > right:                                       # 사과가 바구니 오른쪽에 있다면
        cnt += apple - right
        left += apple - right
        right = apple
    
    elif apple < left:                                      # 사과가 바구니 왼쪽에 있다면
        cnt += left - apple
        right -= left - apple
        left = apple

print(cnt)

'''
회고 / TIL
- TC는 통과되었으나 제출했을 때 틀려서 반례를 찾아보니 사과가 바구니의 오른쪽에 있을 때는 left, right 순서대로 업데이트했는데,
- 사과가 바구니 왼쪽에 있을 때도 동일하게 left, right 순서대로 업데이트하니 right에 바뀐 left가 들어가서 제대로 업데이트되지 않았음.
- 이러한 실수를 하지 않도록 조심해야겠음.
'''