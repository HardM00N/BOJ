# https://www.acmicpc.net/problem/10815

# 나의 풀이 (Python3  780ms)
_ = int(input())
cards = set(map(int, input().split()))                      # 중복이 없으므로 set (in 메서드 시간 줄이기)
_ = int(input())
tests = list(map(int, input().split()))

for test in tests:                  
    if test in cards:                                       # test가 cards에 있으면
        print(1, end=' ')
    else:
        print(0, end=' ')

# 다른 사람의 풀이 (Python3 384ms)
def solution():
    import sys

    A, B = sys.stdin.read().split("\n")[1::2]               # 한 번에 입력받음
    A = set(A.split())
    B = B.split()
    print("".join("1 " if x in A else "0 " for x in B))

solution()

'''
회고 / TIL
- 다른 사람의 풀이와 로직은 같은데, 시간 차이는 2배 가까이 남. 
- 컴프리헨션과 친해지자!
'''