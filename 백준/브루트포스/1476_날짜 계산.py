# https://www.acmicpc.net/problem/1476

# 첫 번째 풀이 (시간 초과)
E, S, M = map(int, input().split())
e, s, m = 1, 1, 1
year = 1

while E != e or S != s or M != m:               # e, s, m이 E, S, M이 될 때까지
    e += 1
    e %= 15                                     # % 연산 활용
    s += 1
    s %= 28
    m += 1
    m %= 19
    year += 1

print(year)

# 두 번째 풀이 (Python3 40ms)
E, S, M = map(int, input().split())
year = 1

while 1:
    if E == 1 and S == 1 and M == 1:            # E, S, M이 1, 1, 1이 될 때까지
        break
    else:
        if E == 1:
            E = 15
        else:
            E -= 1
        if S == 1:
            S = 28
        else:
            S -= 1
        if M == 1:
            M = 19
        else:
            M -= 1
        
        year += 1

print(year)

# 다른 사람의 풀이
e, s, m = map(int, input().split())
all = 15 * 28 * 19
x = (6916 * e + 4845 * s + 4200 * m) % all

if x == 0:
    x = all

print(x)

'''
6916 = 13 x 28 x 19
4845 = 15 x 17 x 19
4200 = 15 x 28 x 10
'''


'''
회고 / TIL
- 처음에 모든 과정에서 % 연산을 하다보니 시간 초과됨.
- 15나 28, 19에 도달했을 때만 연산하도록 수정함.
- 다른 사람의 풀이 이해 불가...
'''