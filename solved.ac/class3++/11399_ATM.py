# https://www.acmicpc.net/problem/11399

# 나의 풀이 (Python3 72ms)
_ = int(input())
P = list(map(int, input().split()))

total, temp = 0, 0

for i in sorted(P):         # 최소의 합을 구하려면 오름차순
    temp += i               # temp는 현재 내가 기다린 시간
    total += temp           # total은 모두가 각자 기다린 시간의 합
print(total)

'''
회고 / TIL
- 오랜만에 힐링 문제... 시간복잡도도 1등이랑 똑같아서 기분 좋음...
'''