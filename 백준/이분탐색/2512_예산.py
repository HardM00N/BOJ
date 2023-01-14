# https://www.acmicpc.net/problem/2512

# 나의 풀이
N = int(input())
needs = list(map(int, input().split()))
cap = int(input())

if sum(needs) <= cap:
    print(max(needs))

else:
    pass