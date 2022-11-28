# https://www.acmicpc.net/problem/17219

# 나의 풀이 (Python3 268ms)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pws = {}                                    # 딕셔너리 선언

for _ in range(N):          
    site, pw = input().split()              # site를 key, pw를 value로 저장
    pws[site] = pw

for _ in range(M):
    print(pws[input().rstrip()])            # 입력된 site의 value 출력


'''
회고 / TIL
- 보자마자 이건 딕셔너리다! 싶어서 풀었음. 
- 다른 풀이보다 시간은 약간 느리지만, 메모리 공간은 적게 차지함. 
'''