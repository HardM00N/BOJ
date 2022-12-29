# https://www.acmicpc.net/problem/1789

# 첫 번째 풀이
from itertools import combinations

S = int(input())
N = 0

nums = [i + 1 for i in range(S)]

for i in range(1, S // 2 + 1):
    for j in combinations(nums, i):
        if sum(j) == S:
            N = i
            break

print(N)

# 두 번째 풀이 (Python3 56ms)
S = int(input())
i, sum = 1, 0                   # 더해줄 자연수와 합계 초기화

while 1:
    sum += i                    # 자연수를 합계에 더함
    
    if sum > S:                 # 합계가 목표치를 초과하면
        print(i - 1)            # 직전의 자연수 출력
        break

    i += 1


'''
회고 / TIL
- 조합으로 접근해서 풀었더니 시간 초과 발생함.
- 다시 차근차근 규칙을 찾으니 쉽게 풀림.
'''