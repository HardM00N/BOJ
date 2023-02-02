# https://school.programmers.co.kr/learn/courses/30/lessons/12969

# 나의 풀이
n, m = map(int, input().split())

for _ in range(m):
    print('*' * n)

# 다른 사람의 풀이
a, b = map(int, input().strip().split(' '))
answer = ('*' * a +'\n') * b                    # for문을 사용하지 않고 개행문자를 바로 사용
print(answer)

'''
회고 / TIL
- 아주 오랜만에 푸는 별찍기라 반가웠음.
- 다양한 풀이 방법을 떠올릴 수 있도록 노력해야겠음.
'''