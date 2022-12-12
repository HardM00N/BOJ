# https://www.acmicpc.net/problem/1193

'''
홀수번째 -> 우상향
짝수번째 -> 좌하향
'''

# 나의 풀이 (Python3 36ms)
X = int(input())

total = 0
temp = 0
cnt = 0                                                 # 몇 번째 대각선인지 카운트

while 1:
    temp += 1
    total += temp
    
    cnt += 1

    if total >= X:
        break

gap = total - X                                         # 대각선의 끝 순번에서 현재 순번이 얼마나 떨어져 있는지

if cnt % 2:
    print('{}/{}'.format(gap + 1, temp - gap))          # 홀수번째 대각선이면 우상향, 분모 감소 / 분자 증가
else:
    print('{}/{}'.format(temp - gap, gap + 1))          # 짝수번째 대각선이면 좌하향, 분모 증가 / 분자 감소

# 다른 사람의 풀이
n = int(input())
c = 1
while n > c:
    n -= c
    c += 1
if c % 2 == 0:
    print(f"{n}/{1 + c - n}")
else:
    print(f"{1 + c - n}/{n}")


'''
회고 / TIL
- 생각보다 푸는데 오래 걸린 문제였음.
- X 번째 분수가 몇 번째 대각선에 위치하는지 찾는 걸 구현하는데 애먹었지만, 푸는데 성공함.
- 다른 사람의 풀이를 보니, 더 간결하게 몇 번째 대각선에 위치하는지를 계산할 수 있었음...
'''