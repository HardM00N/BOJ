# https://www.acmicpc.net/problem/2776

# 나의 풀이 (Python3 1264ms)
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    input()
    note1 = set(input().split())                # note1 받기 (세트)
    input()
    note2 = list(input().split())               # note2 받기 (리스트)

    for num in note2:
        if num in note1:
            print(1)
        else:
            print(0)

# 다른 사람의 풀이 (Python3 860ms)
import sys

for _ in range(int(sys.stdin.readline())):
    N = sys.stdin.readline()
    note_1 = set(sys.stdin.readline().split())
    M = sys.stdin.readline()
    print('\n'.join('1' if i in note_1 else '0' for i in sys.stdin.readline().split()))

'''
회고 / TIL
- 굳이 이분탐색으로 풀지 않아도 되는 문제
- 1등 풀이와 로직은 완전히 같은데, note2를 저장하지 않고 컴프리헨션으로 사용한 부분에서 시간 차이가 많이 발생한 것 같음.
'''