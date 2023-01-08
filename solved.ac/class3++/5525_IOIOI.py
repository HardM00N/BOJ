# https://www.acmicpc.net/problem/5525

# 첫 번째 풀이 (50점, Python3 36ms)
N = int(input())
M = int(input())
S = input()

P = 'IOI' + 'OI' * (N - 1)
cnt = 0

for i in range(M):
    if S[i:i + 3 + 2 * (N - 1)] == P:
        cnt += 1

print(cnt)

# 두 번째 풀이 (100점, Python3 232ms)
N = int(input())
M = int(input())
S = input()

i = 0
cnt = 0
cnt_ioi = 0

while 1:
    if i == M:
        break

    if S[i:i + 3] == 'IOI':
        cnt_ioi += 1
        i += 2
        if cnt_ioi == N:
            cnt += 1
            cnt_ioi -= 1
    else:
        i += 1
        cnt_ioi = 0

print(cnt)

# 다른 사람의 풀이
i = input
n = int(i())
i()
print(sum(max(0, len(s) - n) for s in i().replace('IO', 'X').replace('XI', 'XXO').replace('I', 'O').split('O')))

'''
OOIOIOIOIIOII -> replace('IO', 'X') ->
OOXXXIXII -> replace('XI', 'XXO') ->
OOXXXXOXXOI -> replace('I', 'O') ->
OOXXXXOXXOO -> split('O') -> ['', '', XXXX, XX, '', ''] -> 2
'''

'''
회고 / TIL
- 서브 태스크가 있는 문제는 처음 접해봤는데, 역시 실버1이라 처음에 50점만 맞았음.
- IOIOIOI...를 매번 찾다보면 시간 오래 걸리기 때문에, IOI를 발견한 경우 OI를 붙여가면서 카운트함으로써 해결함.
- 다른 사람의 풀이는 문자를 치환해 XX의 개수를 조사함으로써 카운트함. 저런 식으로 풀 수 있도록 노력하자.
'''