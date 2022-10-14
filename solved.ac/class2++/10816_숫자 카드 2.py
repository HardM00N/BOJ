'''
숫자 카드는 정수 하나가 적혀 있는 카드이다. 
상근이는 숫자 카드 N개를 갖고 있다. 
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 갖고 있는지 구하는 프로그램을 작성하시오. 
'''

# 첫 번째 풀이 (시간 초과)
# import sys

# input = sys.stdin.readline

# _ = input()
# n_list = list(map(int, input().split()))
# _ = input()
# m_list = list(map(int, input().split()))

# for m in m_list:
#     cnt = 0
#     for n in n_list:
#         if m == n:
#             cnt += 1
#     print(cnt, end=' ')

# 두 번째 풀이 (계수 정렬 이용)
import sys
input = sys.stdin.readline

_ = input()
n_list = list(map(int, input().split()))
_ = input()
m_list = list(map(int, input().split()))

nums = [0] * 20000001

for n in n_list:
    nums[n] += 1

for m in m_list:
    print(nums[m], end=' ')

'''
회고 / TIL
- 무턱대고 이중 for문으로 풀었다가 가볍게 시간 초과의 벽에 부딪힘. 
- 저번에 풀었던 계수 정렬 문제가 생각나서 그리 풀었는데 다행히 맞힘. 
- 다른 사람의 풀이를 보니 이분 탐색과 해시를 활용하는 것 같음. 흠...
'''