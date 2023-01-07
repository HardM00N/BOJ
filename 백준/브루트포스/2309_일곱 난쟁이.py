# https://www.acmicpc.net/problem/2309

# 나의 풀이 (Python3 36ms)
from itertools import combinations
import sys
input = sys.stdin.readline

dwarfs = set(int(input()) for _ in range(9))            # 아홉 난쟁이 키를 set에 저장

sum_height = sum(dwarfs)                                # 아홉 난쟁이의 키를 합산

for i in combinations(dwarfs, 2):                       # 제외할 두 난쟁이를 조합해
    if sum_height - sum(i) == 100:                      # 이 두 난쟁이의 키를 뺀 합이 100이라면
        dwarfs -= set(i)                                # 차집합 연산
        break

for dwarf in sorted(dwarfs):                            # 오름차순으로 정렬해 출력
    print(dwarf)

'''
회고 / TIL
- 조합으로 쉽게 풀 수 있는 문제
- 다른 사람의 풀이는 비슷해 생략함.
'''