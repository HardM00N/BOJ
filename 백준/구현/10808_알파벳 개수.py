# https://www.acmicpc.net/problem/10808

# 나의 풀이 (Python3 36ms)
s = input()

for i in 'abcdefghijklmnopqrstuvwxyz':
    print(s.count(i), end=' ')                  # count 활용

# 다른 사람의 풀이
a = [0] * 26
for s in input(): a[ord(s) - 97] += 1           # 계수 정렬 활용
print(*a)

'''
회고 / TIL
- 간단한 문제였음.
'''