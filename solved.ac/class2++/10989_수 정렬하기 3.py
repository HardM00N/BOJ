'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오. 
'''

# 첫 번째 풀이 (메모리 초과)
# nums = []
# for _ in range(int(input())):
#     nums.append(int(input()))

# nums.sort()
# for i in nums:
#     print(i)

# 두 번째 풀이 (계수 정렬 이용)
import sys

input = sys.stdin.readline
num = [0] * 10001

for _ in range(int(input())):
    num[int(input())] += 1

for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)

'''
회고 / TIL
- 무턱대고 쉬운 문제네 하고 sort()로 풀었다가 메모리 초과로 틀렸다. 
- 계수 정렬을 이용해 10000까지의 수의 각 개수를 기록해 출력한다.
- sys.stdin.readline()은 실행 시간을 줄여준다고 하니 익혀보자. 
- sys.stdin.readline()은 prompt message를 출력하지 않고, 개행 문자를 삭제하지 않아서 빠르다고 함. 
'''