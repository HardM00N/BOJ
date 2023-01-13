# https://www.acmicpc.net/problem/11034

# 나의 풀이 (Python3 36ms)
import sys
input = sys.stdin.readline

while 1:
    try:
        A, B, C = map(int, input().split())
        print(max(B - A, C - B) - 1)                # B - A, C - B 중 큰 값에서 -1한 만큼 최대 이동 가능

    except:
        break

# 다른 사람의 풀이
for i in open(0): a, b, c = map(int, i.split());print(max(c - b, b - a) - 1)

'''
회고 / TIL
- 언뜻 복잡해보이지만 갭이 큰 쪽 - 1만큼이 결국 최대로 움직일 수 있는 횟수임.
- 다른 사람의 풀이를 보니 open()으로 TC를 받았음. 참고하자.
'''