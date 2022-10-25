'''
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 
통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자. 

1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오. 
'''

import sys
input = sys.stdin.readline
from collections import Counter

nums = []

for _ in range(int(input())):
    nums.append(int(input()))

print(round(sum(nums) / len(nums)))                         # 산술평균 출력
print(sorted(nums)[len(nums) // 2])                         # 중앙값 출력

cnt = Counter(nums)
mode = cnt.most_common()
mode.sort(key=lambda x: (x[1], -x[0]), reverse=True)        # 최빈값 우선 내림차순 정렬, 최빈값이 같을 경우 수로 오름차순 정렬

if len(mode) > 1:                                           # 최빈값이 여러 개인 경우
    if mode[0][1] == mode[1][1]:                            
        print(mode[1][0])                                   # 최빈값 중 두 번째로 작은 값 출력
    else:
        print(mode[0][0])                                       
else:
    print(mode[0][0])                                       # 최빈값이 여러 개가 아니라면 바로 출력

print(max(nums) - min(nums))                                # 범위 출력

'''
회고 / TIL
- 쉬워 보였으나 의외로 애먹은 문제임. 
- 최빈값이 가장 까다로웠음. Counter를 사용하고, 정렬 조건을 다르게 설정한 sort를 이용해 풀었음. 
- sort에 lambda를 사용할 때, 조건에 -를 붙이면 내림차순 정렬이 가능하다는 사실을 검색을 통해 알게됨. (매우 유용할 듯)
'''