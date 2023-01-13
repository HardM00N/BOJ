# https://www.acmicpc.net/problem/2920

# 나의 풀이 (Python3 36ms)
s = input()

if s == '1 2 3 4 5 6 7 8': print('ascending')
elif s == '8 7 6 5 4 3 2 1': print('descending')
else: print('mixed')

# 나의 예전 풀이 (Python3 32ms)
nums = list(map(int, input().split()))

asc = [1, 2, 3, 4, 5, 6, 7, 8]
des = list(reversed(asc))

if nums == asc:
    print('ascending')
elif nums == des:
    print('descending')
else:
    print('mixed')

'''
회고 / TIL
- 예전에 풀었던 문제를 다시 풀었는데, 정렬을 이용하지 않고 단순 문자열 비교로 풀어봤음.
- 시간은 정렬이 약간 더 빠름.
'''