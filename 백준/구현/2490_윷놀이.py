# https://www.acmicpc.net/problem/2490

# 나의 풀이 (Python3 32ms)
res = ['D', 'C', 'B', 'A', 'E']

for _ in range(3):
    print(res[sum(list(map(int, input().split())))])        # 등의 합에 따라 출력

'''
회고 / TIL
- 단순히 리스트의 합에 따라 결과를 출력하면 됨.
- res를 리스트로 두는 것이 str 'DCBAE'로 두는 것보다 4ms 빠름. (str -> 리스트화 하는 과정이 불필요해서 그런 듯)
'''