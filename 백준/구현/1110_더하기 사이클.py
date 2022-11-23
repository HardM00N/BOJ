# https://www.acmicpc.net/problem/1110

# 나의 풀이
N = input()

if len(N) == 1:                                 # N이 한 자리라면, 앞에 0을 붙임 
        N = '0' + N

num = N                                         # 반복문에서 계속 변할 숫자를 담을 변수
cnt = 0                                         # 사이클을 측정할 변수

while 1:
    sum = str(int(num[0]) + int(num[1]))        # 한 자리씩 덧셈
    
    if len(sum) == 1:                           # 덧셈 결과도 한 자리라면, 앞에 0을 붙임
        sum = '0' + sum
    
    num = num[1] + sum[1]                       # 새로운 num 업데이트
    cnt += 1                                    # 더하기 사이클 + 1

    if num == N:                                # 새로 만들어진 num이 원래의 N이라면, 종료
        break

print(cnt)

# 다른 사람의 풀이
n = int(input())                                # 애초에 int형으로 받음
m = n                                           # 반복문에서 계속 변할 숫자를 담을 변수
i = 0                                           # 사이클을 측정할 변수
while True:
    m = m % 10 * 10 + (m % 10 + m // 10) % 10   # 원래 1의 자리를 10의 자리로, 각 자리의 덧셈 결과를 1의 자리로
    i += 1
    if m == n:
        break
print(i)

'''
회고 / TIL
- 더하기 사이클이라는 개념이 신박했음. 
- 이렇게 숫자 각 자리끼리 합을 구하는 비슷한 문제를 저번에는 int형으로 풀어서, 이번엔 str형으로 풀었음. 
- 문제를 이해하고 차근차근 구현하면 쉽게 풀리는 문제임. 
- 다른 사람의 풀이를 보니 int형으로 푼 케이스가 많은 것 같음. 
'''